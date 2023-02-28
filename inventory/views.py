#<!--Source: Example HTML code from https://github.com/KenBroTech/Django-Inventory-Management-System-->
from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url = 'login')
def DashboardView(request):
	return render(request, 'dashboard/dashboard.html')
	
@login_required(login_url = 'login')
def staff(request):
	return render(request, 'dashboard/staff.html')

@login_required(login_url = 'login')
def product(request):
	return render(request, 'dashboard/product.html')

@login_required(login_url = 'login')
def order(request):
	return render(request, 'dashboard/order.html')

