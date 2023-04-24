from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.template import loader

# Create your views here.

#class GenericView(generic.ListView):
#    template_name = "index.html"

def mainPage(request):
    response = loader.get_template('index.html')
    food = ['Spagetti', 15, 'Fish and chips', 18, 'Beef Burger', 21, 'Irish Breakfast', 12]
    context = {
        'foods' : food
    }
    return HttpResponse(response.render(context, request))

