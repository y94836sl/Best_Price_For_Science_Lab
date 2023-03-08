#<!--Source: Example HTML code from https://github.com/KenBroTech/Django-Inventory-Management-System-->
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import requests
from django.contrib.auth.decorators import login_required
from .models import Product, Order, PotentialProduct
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
	LowInStockProducts = products.count()
	recent_PotentialProducts = PotentialProduct.objects.all().order_by('-id')[:2]
	
	LowInStockProducts = products.filter(quantity__lt=10)[:2]
	
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
		'recent_PotentialProducts': recent_PotentialProducts,
		'LowInStockProducts': LowInStockProducts,
	}
	return render(request, 'dashboard/dashboard.html', context)

def update_product_info(request):
	if request.method == 'POST':
		product_name = request.POST.get('product_name')
		product_price = request.POST.get('product_price')
		product_url = request.POST.get('product_url')
		
		# Update the product information
		PotentialProduct = PotentialProduct(
					staff=request.user,
					name=product_name,
					price=product_price,
					url=product_url
				)
		PotentialProduct.save()
		
		context = {
			'product_name': product_name,
			'product_price': product_price,
			'product_url': product_url,
		}
		
		render(request, 'dashboard/dashboard.html', context)
	return JsonResponse({'success': False})

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
	LowInStockProducts = Product.objects.all().filter(quantity__lt=10)[:2]
	
	context = {
		'employees': employees,
		'employeesNum': employeesNum,
		'ordersNum': ordersNum,
		'productsNum': productsNum,
		'LowInStockProducts': LowInStockProducts,
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
	LowInStockProducts = Product.objects.all().filter(quantity__lt=10)[:2]
	
	context = {
		'items':items,
		'employeesNum':employeesNum,
		'ordersNum':ordersNum,
		'productsNum':productsNum,
		'LowInStockProducts':LowInStockProducts,
	}
	
	return render(request, 'dashboard/product.html', context)

@login_required(login_url = 'login')
def product_add(request):
	items = Product.objects.all() # Use ORM
	
	# ------- Satisitc ------- 
	ordersNum = Order.objects.all().count()
	productsNum = Product.objects.all().count()
	employeesNum = CustomUser.objects.all().count()
	LowInStockProducts = Product.objects.all().filter(quantity__lt=10)[:2]
	
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
		'LowInStockProducts':LowInStockProducts,
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
	LowInStockProducts = Product.objects.all().filter(quantity__lt=10)[:2]
	
	context = {
			'orders': orders,
			'employeesNum': employeesNum,
			'ordersNum': ordersNum,
			'productsNum': productsNum,
			'LowInStockProducts': LowInStockProducts,
		}
	return render(request, 'dashboard/order.html', context)



