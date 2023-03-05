from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Different categories of products
CATEGORY = (
	('Stationary','Stationary'),
	('Electronics','Electronics'),
	('Chemical','Chemical'),
	('Safety','Safety'),
)

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=200, null=True)
	category = models.CharField(max_length=20, choices=CATEGORY, null=True)
	quantity = models.PositiveIntegerField(null=True)
	price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
	url = models.URLField(blank=True)
	
	# Change the display in the admin table
	def __str__(self):
		return f'{self.name}--[{self.quantity}]'
	
class Order(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
	staff = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, null=True)
	order_quantity = models.PositiveIntegerField(null=True)
	date = models.DateTimeField(auto_now_add=True)
	
	# Change the display in the admin table
	def __str__(self):
		return f'{self.product} ordered by {self.staff.username}'