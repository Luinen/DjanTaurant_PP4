from django.db import models
from django import forms
from datetime import datetime    
from cloudinary.models import CloudinaryField
from django.utils import timezone

# Create your models here.

class User(models.Model):
    # user_id
    user_firstname = models.CharField(max_length=50)
    user_lastname = models.CharField(max_length=50)
    user_username = models.CharField(max_length=100)
    user_email = models.EmailField('email address', max_length=100, unique=True)
    user_password = models.CharField(max_length=50)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)


#class UserForm(forms.ModelForm):
#    password = forms.CharField(widget=forms.PasswordInput)
#    class Meta:
#        model = User

