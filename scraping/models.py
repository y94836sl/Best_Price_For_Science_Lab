from django.db import models

# Create your models here.
class Products(models.Model):
	name = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	link = models.CharField(max_length=2083, default="", unique=True)
	supplier = models.CharField(max_length=30, default="", blank=True, null=True)