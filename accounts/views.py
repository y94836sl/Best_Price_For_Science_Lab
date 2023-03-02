from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
import requests
from django.contrib.auth.decorators import login_required

# Create your views here.
class SignUpView(CreateView):
	form_class = CustomUserCreationForm 
	success_url = reverse_lazy('login') 
	template_name = 'registration/signup.html'

@login_required(login_url = 'login')
def ProfileView(request):
	context = {
		
	}
	return render(request, 'registration/profile.html',context)