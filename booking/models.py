from django.db import models
from django import forms
from datetime import datetime
from cloudinary.models import CloudinaryField
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

'''
class User(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=100)
    email = models.EmailField('email address', max_length=100, unique=True)
    password = models.CharField(max_length=50)
    date_joined = models.DateTimeField(default=timezone.now)


class Staff(models.Model):
    email = models.EmailField('email address', max_length=100, unique=True)
'''

class Food(models.Model):

    name = models.CharField(max_length=80)
    ingredients = models.CharField(max_length=100)
    price = models.IntegerField()
    picture = models.ImageField()
    state = models.BooleanField(default=True)
    # self.allergens.all = models.ManyToManyField(Allergen)
    leiras = models.CharField(max_length=20)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    # def get_allergen_names(self):
    #    return ",".join([str(allergen) for allergen in self.allergens.all()])

    # allergen = models.CharField(max_length=200, blank=True, null=True, default=get_allergen_names)


class Allergen(models.Model):
    allergen_name = models.CharField(max_length=25)
    food_name = models.CharField(max_length=80)

    def __str__(self):
        return self.allergen_name

'''
class Table(models.Model):
    table_id = models.AutoField()
    restaurant_name = models.CharField(max_length=30)
    capacity = models.IntegerField()

    #def __str__(self):
    #    return self.restaurant_name
'''

class Capacity(models.Model):
    name = models.CharField(max_length=30, primary_key= True)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Booking(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Capacity, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    guest_number = models.IntegerField()

    def __str__(self):
        return self.user.username +' '+ str(self.guest_number) +' '+ self.datetime.strftime("%m/%d/%Y, %H:%M:%S")
