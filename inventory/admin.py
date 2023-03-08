from django.contrib import admin
from .models import Product, Order, PotentialProduct
from django.contrib.auth.models import Group

# Change the admin page header
admin.site.site_header = 'LabSaver Adminstration'

# Change the display list and add filter for admin
class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'quantity', 'category',)
	list_filter = ('category',)
	
	
# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(PotentialProduct)

