from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.template import loader
from booking.models import Food

# Create your views here.

#class GenericView(generic.ListView):
#    template_name = "index.html"

def mainPage(request):
    response = loader.get_template('index.html')
    food = Food.objects.all()
    context = {
        'foods' : food
    }
    return HttpResponse(response.render(context, request))

def signUp(request):
    response = loader.get_template('sign_up')
    return HttpResponse(response.render(context, request))
