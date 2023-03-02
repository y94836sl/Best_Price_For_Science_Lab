from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


# Create your models here.
class CustomUser(AbstractUser):
	age = models.PositiveIntegerField(null=True, blank=True)

class Profile(models.Model):
	staff = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
	phone = models.CharField(max_length=20, null=True)
	address = models.CharField(max_length=200, null=True)
	image = models.ImageField(default="defaultProfileImage.jpeg", upload_to="Profile_Images")
	
	def __str__(self):
		return f'{self.staff.username}\'s Profile'