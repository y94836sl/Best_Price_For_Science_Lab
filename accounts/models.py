from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)

class Profile(models.Model):
    staff = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=200, null=True)
    image = models.ImageField(default="defaultProfileImage.jpeg", upload_to="Profile_Images", null=True)

    def __str__(self):
        return f'{self.staff.username}\'s Profile'

class PotentialProduct(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    url = models.URLField(blank=True)
    
    # Change the display in the admin table
    def __str__(self):
        return f'{self.name}'
    