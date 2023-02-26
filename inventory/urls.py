from django.urls import path
from .views import DashboardView, staff, product, order

urlpatterns = [
	path('', DashboardView, name='dashboard'),
	path('staff/', staff, name='staff'),
	path('product/', product, name='product'),
	path('order/', order, name='order'),
]