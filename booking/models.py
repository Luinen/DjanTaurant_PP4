from django.db import models
from django import forms
from datetime import datetime
from cloudinary.models import CloudinaryField
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

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


class Allergen(models.Model):
    allergen_name = models.CharField(max_length=25)
    food_name = models.CharField(max_length=80)

    def __str__(self):
        return self.allergen_name

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
