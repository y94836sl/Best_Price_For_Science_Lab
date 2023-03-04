from django.urls import path
from .views import DashboardView, staff, product, order, product_add

urlpatterns = [
	path('', DashboardView, name='dashboard'),
	path('staff/', staff, name='staff'),
	path('product/', product, name='product'),
	path('product/add', product_add, name='product_add'),
	path('order/', order, name='order'),
]