from django.contrib import admin
from .models import *

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    pass

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    pass
@admin.register(Ticket)
class Ticketdmin(admin.ModelAdmin):
    pass
@admin.register(Analyse)
class AnalyseAdmin(admin.ModelAdmin):
    pass



