from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


    
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name','email','age']