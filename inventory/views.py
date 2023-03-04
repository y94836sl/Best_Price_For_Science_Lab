#<!--Source: Example HTML code from https://github.com/KenBroTech/Django-Inventory-Management-System-->
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm
from accounts.models import CustomUser

# Create your views here.
@login_required(login_url = 'login')
def DashboardView(request):
	return render(request, 'dashboard/dashboard.html')

# ------------------------------------------
# ------------------ Staff -----------------
# ------------------------------------------
@login_required(login_url = 'login')
def staff(request):
	employees = CustomUser.objects.all()
	context = {
		'employees': employees
	}
	return render(request, 'dashboard/staff.html', context)

@login_required(login_url = 'login')
def staff_detail(request, pk):
	employee = CustomUser.objects.get(id=pk)
	context = {
		'employee': employee
	}
	return render(request, 'dashboard/staff_detail.html', context)

# ---------------------------------------------
# ------------------ Product ------------------
# ---------------------------------------------￼

@login_required(login_url = 'login')
def product(request):
	items = Product.objects.all() # Use ORM
#	items = Product.objects.raw('SELECT * from product')
	context = {
		'items':items,
	}
	
	return render(request, 'dashboard/product.html', context)

@login_required(login_url = 'login')
def product_add(request):
	items = Product.objects.all() # Use ORM
	if request.method == 'POST':
		form = ProductForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('product')
	else:
		form = ProductForm()
		
	context = {
		'items':items,
		'form': form,
	}
	return render(request, 'dashboard/product_add.html', context)

@login_required(login_url = 'login')
def product_delete(request, pk):
	item = Product.objects.get(id=pk) # Use ORM
	if request.method == 'POST':
		item.delete()
		return redirect('product')
	context = {
		'item': item,
	}
	return render(request, 'dashboard/product_delete.html', context)

@login_required(login_url='login')
def product_update(request, pk):
	item = Product.objects.get(id=pk) # Use ORM
	if request.method == "POST":
		form = ProductForm(request.POST, instance=item)
		if form.is_valid():
			form.save()
			return redirect('product')
	else:
		form = ProductForm(instance=item)
	context = {
		'form': form,
		'item': item,
	}
	return render(request, 'dashboard/product_update.html', context)

# ------------------------------------------￼-
# ------------------ Order ------------------
# -------------------------------------------
@login_required(login_url = 'login')
def order(request):
	return render(request, 'dashboard/order.html')



