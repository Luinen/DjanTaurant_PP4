from django.db import models
from django import forms
from datetime import datetime    
from cloudinary.models import CloudinaryField
from django.utils import timezone

# Create your models here.

class User(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=100)
    email = models.EmailField('email address', max_length=100, unique=True)
    password = models.CharField(max_length=50)
    date_joined = models.DateTimeField(default=timezone.now)
    #is_staff = models.BooleanField(default=False)

class Staff(models.Model):
    email = models.EmailField('email address', max_length=100, unique=True)

#class UserForm(forms.ModelForm):
#    password = forms.CharField(widget=forms.PasswordInput)
#    class Meta:
#        model = User

class Food(models.Model):

    #MILK = 1
    #EGG = 2
    #PEANUTS = 3
    #FLOUR = 4

    #ALLERGY_CHOICES = (
    #    (0, 'None'),
    #    (1, 'Milk'),
    #    (2, 'Egg'),
    #    (3, 'Peanuts'),
    #    (4, 'Flour'),
    #)

    name = models.CharField(max_length=80)
    ingredients = models.CharField(max_length=100)
    #allergy = models.IntegerField(choices=ALLERGY_CHOICES, default=0)
    price = models.IntegerField()
    picture = models.ImageField()
    state = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name



class Allergen(models.Model):
    allergen_name = models.CharField(max_length=25)
    food_name = models.CharField(max_length=80)
    



#class Tables(models.Model):
#    tables_seat = models.IntegerField.choices()

# class Booking(models.Model):
#   booking_user_id
#   booking_seat_id
#   booking_datetime
#   booking_status 0 new 1 rejected 2 accepted
