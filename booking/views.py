from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.template import loader
from booking.models import Food, Booking, Table
from django import forms

# Create your views here.


def mainPage(request):
    response = loader.get_template('index.html')
    food = Food.objects.all()[:4]
    context = {
        'foods': food
    }
    return HttpResponse(response.render(context, request))


class Reservation(View):

    def get(self, request):
        return render(request, "reservation.html")


class ReservationForm(forms.Form):
    reservation_start = forms.DateTimeField(label="Start of Reservation")
    guests = forms.IntegerField(label="Number of Guests")
    


def bookingCreate(request):
    print("/////////////////////////////")
    form = ReservationForm(request.POST)
    print(form.is_valid())
    if form.is_valid():
        return HttpResponse("Thank You")
    else:
        return HttpResponse("No reservation made")
     #   print(form.cleaned_data["reservation_start"])
    #return HttpResponseRedirect("reservation/")


class Menu(View):

    def get(self, request):
        food = Food.objects.all()
        context = {
            'foods': food
            }
        return render(request, "menu.html", context=context)

