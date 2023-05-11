from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import UserChangeForm,UserCreationForm
# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ['first_name','last_name','username','email','age','is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None,{'fields':('age',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields':('age',)}), 
    )

admin.site.register(CustomUser,CustomUserAdmin)
