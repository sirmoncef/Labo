from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.utils import timezone
from django.core.exceptions import ValidationError

class Exam(models.Model):
    exam = models.CharField(max_length=200)
    tube = models.CharField(max_length=100)
    price = models.IntegerField()
    

    def __str__(self) :
        return self.exam




class Appointment(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=10)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    first_time = models.BooleanField(default=False)
    comments = models.TextField(blank=True, null=True)

class Ticket(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    number = models.IntegerField(unique=True)
    
    def save(self, *args, **kwargs):
        if not self.number:
            last = Ticket.objects.order_by('-number').first()
            self.number = last.number + 1 if last else 1
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Ticket #{self.number}"
    

class Analyse(models.Model):
    result = models.ImageField(upload_to='analyses/', null=True, blank=True)
    code = models.IntegerField()
    
    def __str__(self):
        return f"Analysis #{self.code}"
    

    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Message from {self.name} ({self.email})"
    
    class Meta:
        ordering = ['-created_at']


    

