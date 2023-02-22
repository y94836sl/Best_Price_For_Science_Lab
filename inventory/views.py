from django.shortcuts import render
import requests

# Create your views here.
def DashboardView(request):
	return render(request, 'dashboard.html')
	