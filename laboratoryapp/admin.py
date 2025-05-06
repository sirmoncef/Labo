from django.contrib import admin
from .models import *

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    pass

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
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

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)

