from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

class HomeView(TemplateView):
    template_name: str = 'home/home.html'

class LoginInterfaceView(LoginView):
    template_name: str = 'home/login.html'
    success_url = '/admin/'

class LogoutInterfaceView(LogoutView):
    template_name: str = 'home/logout.html'