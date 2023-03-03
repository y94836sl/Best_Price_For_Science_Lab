from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm, UserUpdateForm, ProfileUpdateForm
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

def ProfileUpdate(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(
			request.POST, request.FILES, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
		
	context = {
		'u_form': u_form,
		'p_form': p_form,
	}
	return render(request, 'registration/profile_update.html', context)