
from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('services/services/', views.services, name='services'),
    path('services/appointment/', views.appointment, name='appointment'),
    path('services/getanalyses/', views.get_analysis, name='get_analysis'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('contact/', views.contact_view, name='contact'),


]


