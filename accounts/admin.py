from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm 
from .models import CustomUser, Profile

# Register your models here.
class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm 
	form = CustomUserChangeForm 
	model = CustomUser
	# To control the filed listed in http://127.0.0.1:8000/admin/accounts/customuser/
	lsit_display = ['email', 'username', 'age', 'is_staff',]
	# To edit and add new custom fields
	fieldsets = UserAdmin.fieldsets + (
		(None, {'fields':('age',)}),
	)
	
	add_fieldsets = UserAdmin.add_fieldsets + (
		(None, {'fields' : ('age',)}),
	)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
