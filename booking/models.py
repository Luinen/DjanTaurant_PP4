from django.db import models
from django import forms
from datetime import datetime    
from cloudinary.models import CloudinaryField
from django.utils import timezone

# Create your models here.

class User(models.Model):
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

class Food(models.Model):

    MILK = 1
    EGG = 2
    PEANUTS = 3
    FLOUR = 4

    ALLERGY_CHOICES = (
        (0, 'None'),
        (1, 'Milk'),
        (2, 'Egg'),
        (3, 'Peanuts'),
        (4, 'Flour'),
    )

    food_name = models.CharField(max_length=80)
    food_ingredients = models.CharField(max_length=100)
    food_allergy = models.IntegerField(choices=ALLERGY_CHOICES, default=0)
    food_price = models.IntegerField()
    food_picture = models.ImageField()
    food_state = models.BooleanField(default=True)




# class Allergy



#class Tables(models.Model):
#    tables_seat = models.IntegerField.choices()

# class Booking(models.Model):
#   booking_user_id
#   booking_seat_id
#   booking_datetime
#   booking_status 0 new 1 rejected 2 accepted
