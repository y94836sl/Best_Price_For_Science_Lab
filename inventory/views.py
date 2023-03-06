#<!--Source: Example HTML code from https://github.com/KenBroTech/Django-Inventory-Management-System-->
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm, OrderForm
from accounts.models import CustomUser
from django.contrib import messages


# Create your views here.

# ------------------------------------------
# --------------- Dashboard ----------------
# ------------------------------------------
@login_required(login_url = 'login')
def DashboardView(request):
	orders = Order.objects.all()
	products = Product.objects.all()
	
	# ------- Satisitc ------- 
	employeesNum = CustomUser.objects.all().count()
	ordersNum = orders.count()
	productsNum = products.count()
	
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			# Add the staff info into the form
			instance = form.save(commit=False)
			instance.staff = request.user
			instance.save()
			return redirect('dashboard')
	else:
		form = OrderForm()
	context = {
		'form': form,
		'orders': orders,
		'products': products,
		'employeesNum': employeesNum,
		'ordersNum': ordersNum,
		'productsNum': productsNum,
	}
	return render(request, 'dashboard/dashboard.html', context)

# ------------------------------------------
# ------------------ Staff -----------------
# ------------------------------------------
@login_required(login_url = 'login')
def staff(request):
	employees = CustomUser.objects.all()
	employeesNum = employees.count()
	
	# ------- Satisitc ------- 
	ordersNum = Order.objects.all().count()
	productsNum = Product.objects.all().count()
	
	context = {
		'employees': employees,
		'employeesNum': employeesNum,
		'ordersNum': ordersNum,
		'productsNum': productsNum,
	}
	return render(request, 'dashboard/staff.html', context)

@login_required(login_url = 'login')
def staff_detail(request, pk):
	employee = CustomUser.objects.get(id=pk)
	
	# ------- Satisitc ------- 
	ordersNum = Order.objects.all().count()
	productsNum = Product.objects.all().count()
	employeesNum = CustomUser.objects.all().count()
	
	context = {
		'employee': employee,
		'ordersNum': ordersNum,
		'productsNum': productsNum,
		'employeesNum': employeesNum,
	}
	return render(request, 'dashboard/staff_detail.html', context)

# ---------------------------------------------
# ------------------ Product ------------------
# ---------------------------------------------￼

@login_required(login_url = 'login')
def product(request):
	items = Product.objects.all() # Use ORM
#	items = Product.objects.raw('SELECT * from product')
	
	# ------- Satisitc ------- 
	ordersNum = Order.objects.all().count()
	productsNum = Product.objects.all().count()
	employeesNum = CustomUser.objects.all().count()
	
	context = {
		'items':items,
		'employeesNum':employeesNum,
		'ordersNum':ordersNum,
		'productsNum':productsNum,
	}
	
	return render(request, 'dashboard/product.html', context)

@login_required(login_url = 'login')
def product_add(request):
	items = Product.objects.all() # Use ORM
	
	# ------- Satisitc ------- 
	ordersNum = Order.objects.all().count()
	productsNum = Product.objects.all().count()
	employeesNum = CustomUser.objects.all().count()
	
	if request.method == 'POST':
		form = ProductForm(request.POST)
		if form.is_valid():
			form.save()
			product_name = form.cleaned_data.get('name')
			messages.success(request, f'{product_name} has been added !')
			return redirect('product')
	else:
		form = ProductForm()
		
	context = {
		'items':items,
		'form': form,
		'employeesNum':employeesNum,
		'ordersNum':ordersNum,
		'productsNum':productsNum,
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
	orders = Order.objects.all()
	
	# ------- Satisitc ------- 
	ordersNum = orders.count()
	productsNum = Product.objects.all().count()
	employeesNum = CustomUser.objects.all().count()
	
	context = {
			'orders': orders,
			'employeesNum': employeesNum,
			'ordersNum': ordersNum,
			'productsNum': productsNum,
		}
	return render(request, 'dashboard/order.html', context)



