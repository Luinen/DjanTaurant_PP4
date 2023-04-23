from django.shortcuts import render
from django.views import generic

# Create your views here.

class GenericView(generic.ListView):
    template_name = "index.html"