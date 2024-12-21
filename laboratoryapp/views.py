from django.shortcuts import render , redirect
from django.utils import timezone
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login , logout as auth_logout
from django.contrib.auth.hashers import make_password

def home(request):
    return render(request,'home.html')

@login_required
def services(request):
    services = Exam.objects.all()


    return render(request,'laboP3.html',{'services':services,})

@login_required
def appointment(request):
    message = ""
    ticket_number = None

    if request.method == 'POST':
        first_name = request.POST.get('name')
        last_name = request.POST.get('name2')
        phonenumber = request.POST.get('tel')
        email = request.POST.get('em')
        first_time = request.POST.get('q') == 'y'
        date = request.POST.get('date')

        if date:
            
            appointment = Appointment.objects.create(
                first_name=first_name,
                last_name=last_name,
                phonenumber=phonenumber,
                email=email,
                date=date,
                first_time=first_time
            )

            # Create a ticket
            today = timezone.now().date()
            existing_tickets_today = Ticket.objects.filter(appointment__date=today)
            ticket_number = existing_tickets_today.count() + 1
            Ticket.objects.create(appointment=appointment, number=ticket_number)

            message = "Form valid, thank you"
        else:
            message = "Date is required"

    return render(request, 'laboP2.html', {'message': message, 'ticket_number': ticket_number})


@login_required
def get_analysis(request):
    result = None
    error = None
    
    if request.method == 'GET' and 'patientCode' in request.GET:
        code = request.GET.get('patientCode')
        try:
            analysis = Analyse.objects.get(code=code)
            result = analysis.result
        except Analyse.DoesNotExist:
            error = "No valid code found."

    return render(request, 'laboP4.html', {'result': result, 'error': error})


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
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=make_password(password),  
            )
            user.save()
            message = "Thank you for signing up! Please log in."
            return render(request, 'registration/signup.html', {'message': message})
        else:
            message = "Passwords do not match"
            return render(request, 'registration/signup.html', {'message': message})

    return render(request, 'registration/signup.html')


def logout(request):
    auth_logout(request)
    return redirect('home')

