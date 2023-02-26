#<!--Source: Example HTML code from https://github.com/KenBroTech/Django-Inventory-Management-System-->
from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def DashboardView(request):
	return render(request, 'dashboard/dashboard.html')
	
def staff(request):
	return render(request, 'dashboard/staff.html')

def product(request):
	return render(request, 'dashboard/product.html')

def order(request):
	return render(request, 'dashboard/order.html')

