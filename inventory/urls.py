from django.urls import path
from .views import DashboardView, staff, product, order, product_add, product_delete, product_update, staff_detail, update_product_info

urlpatterns = [
	path('', DashboardView, name='dashboard'),
	path('staff/', staff, name='staff'),
	path('staff/detail/<int:pk>/', staff_detail, name='staff_detail'),
	path('product/', product, name='product'),
	path('product/add', product_add, name='product_add'),
	path('product/delete/<int:pk>/', product_delete, name='product_delete'),
	path('product/update/<int:pk>/', product_update, name='product_update'),
	path('order/', order, name='order'),
	path('update_product_info/', update_product_info, name='update_product_info'),
]