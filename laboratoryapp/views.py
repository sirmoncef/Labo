from django.shortcuts import render , redirect
from django.db import transaction
from django.utils import timezone
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login , logout as auth_logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def home(request):
    return render(request,'home.html')


def services(request):
    services = Exam.objects.all()


    return render(request,'laboP3.html',{'services':services,})


def appointment(request):
    message = ""
    ticket_number = None
    appointment_obj = None  # Changed variable name to avoid conflict

    if request.method == 'POST':
        try:
            with transaction.atomic():
                # Create appointment
                appointment_obj = Appointment.objects.create(
                    first_name=request.POST.get('firstName', '').strip(),
                    last_name=request.POST.get('lastName', '').strip(),
                    phonenumber=request.POST.get('phone', '').strip(),
                    email=request.POST.get('email', '').strip(),
                    date=request.POST.get('appointmentDate'),
                    time=request.POST.get('appointmentTime'),
                    first_time=request.POST.get('firstVisit') == 'yes',
                    comments=request.POST.get('comments', '').strip()
                )

                # Create ticket
                ticket = Ticket.objects.create(appointment=appointment_obj)
                ticket_number = ticket.number

                message = "Appointment booked successfully!"
                Notification.objects.create(message=message)

                channel_layer = get_channel_layer()
                async_to_sync(channel_layer.group_send)(
                  "notifications",
                  {
                    "type": "send_notification",
                    "message": "Appointment booked successfully!",
                  }
                )

                
        except Exception as e:
            message = f"Error: {str(e)}"

    return render(request, 'laboP2.html', {
        'message': message,
        'ticket_number': ticket_number,
        'appointment': appointment_obj  # Pass the appointment object
    })




def get_analysis(request):
    result = None
    error = None
    
    if request.method == 'GET' and 'patientCode' in request.GET:
        code = request.GET.get('patientCode')
        try:
            analysis = Analyse.objects.get(code=code)
            result = analysis.result.url if analysis.result else None
        except Analyse.DoesNotExist:
            error = "No valid code found."

    return render(request, 'laboP4.html', {'result': result, 'error': error})


def contact_view(request):
    if request.method == 'POST':
        try:
            # Create and save contact
            Contact.objects.create(
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                phone=request.POST.get('phone'),
                message=request.POST.get('message')
            )
            messages.success(request, "Your message has been sent successfully! We'll contact you soon.")
            return redirect('home')
            
        except Exception as e:
            messages.error(request, f"Couldn't send message. Error: {str(e)}")
    
    return render(request, 'home.html')



def login(request):
    message = ""
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            message = "Invalid username or password"
            
    
    return render(request, 'registration/login.html', {'message': message})


def signup(request):
    message = None  # Initialize message as None
    
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                message = "Username already exists"
            else:
                try:
                    user = User.objects.create(
                        first_name=first_name,
                        last_name=last_name,
                        username=username,
                        email=email,
                        password=make_password(password),
                    )
                    
                    return redirect('login')  
                except Exception as e:
                    message = f"Error creating account: {str(e)}"
        else:
            message = "Passwords do not match"
    
    return render(request, 'registration/signup.html', {'message': message})


def logout(request):
    auth_logout(request)
    return redirect('home')




