from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views import generic

class HomePageView(TemplateView):
	template_name = "home.html"

class AboutPageView(TemplateView):
	template_name = "about.html"
	
class LoginPageView(generic.CreateView):
	success_url = reverse_lazy('home')
	template_name = "registration/login.html"
	
#class SignUpPageView(TemplateView):
#	template_name = "signup.html"