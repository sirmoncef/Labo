from django import forms
from .models import *

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['phonenumber', 'date', 'first_time'] 

