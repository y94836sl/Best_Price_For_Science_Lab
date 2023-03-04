from django.urls import path
from .views import DashboardView, staff, product, order, product_add, product_delete, product_update

urlpatterns = [
	path('', DashboardView, name='dashboard'),
	path('staff/', staff, name='staff'),
	path('product/', product, name='product'),
	path('product/add', product_add, name='product_add'),
	path('product/delete/<int:pk>/', product_delete, name='product_delete'),
	path('product/update/<int:pk>/', product_update, name='product_update'),
	path('order/', order, name='order'),
]