from django.db import models
from django.contrib.auth.models import User


class Exam(models.Model):
    exam = models.CharField(max_length=200)
    tube = models.CharField(max_length=100)
    price = models.IntegerField()
    

    def __str__(self) :
        return self.exam




class Appointment(models.Model):
    first_name = models.CharField(max_length=100,default='hh')
    last_name = models.CharField(max_length=100,default='ggg')
    phonenumber = models.CharField(max_length=10)
    email = models.EmailField(max_length = 254, default='default@example.com')
    date = models.DateField()
    first_time= models.BooleanField(default=False)


    def __str__(self) :

        return f"Appointment for {self.first_name} on {self.date}"
    

class Ticket(models.Model):
    appointment = models.ForeignKey(Appointment,on_delete=models.CASCADE)
    number = models.IntegerField()
    
    
    def __str__(self):
        return f"Ticket {self.number} for {self.appointment.first_name}"
    

class Analyse(models.Model):
    result = models.TextField(max_length=1000)
    code = models.IntegerField()
    
    def __str__(self) :
        return self.result    
    

    
    

    

