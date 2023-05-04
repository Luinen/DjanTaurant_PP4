from django.contrib import admin
from .models import User, Staff, Food, Allergen, Booking, Table

# Register your models here.
admin.site.register(Food)
admin.site.register(Booking)
admin.site.register(Table)