from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import User, Staff, Food, Allergen, Booking, Table

# Register your models here.

#@admin.register(Food)
#class FoodAdmin(SummernoteModelAdmin):


admin.site.register(Food)
admin.site.register(Booking)
admin.site.register(Table)