from django.db import models

CATEGORY = (
	('Stationary','Stationary'),
	('Electronics','Electronics'),
	('Chemical','Chemical'),
	('Safety','Safety'),
)

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=200)
	category = models.CharField(max_length=20)
	quantity = models.PositiveIntegerField()