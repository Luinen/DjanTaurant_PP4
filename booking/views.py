from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.views import View
from django.template import loader
from booking.models import Food

# Create your views here.

def mainPage(request):
    response = loader.get_template('index.html')
    food = Food.objects.all()
    context = {
        'foods' : food
    }
    return HttpResponse(response.render(context, request))


class Reservation(View):

    def get(self, request):
        return render(request, "reservation.html")