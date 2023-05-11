from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.template import loader
from django import forms
from .forms import ReservationForm
from datetime import datetime as dt
from booking.models import Food, Booking, Table
from django.contrib import messages

# Create your views here.


def mainPage(request):
    response = loader.get_template('index.html')
    food = Food.objects.all()[:4]
    context = {
        'foods': food
    }
    return HttpResponse(response.render(context, request))


class Reservation(View):

    form = ReservationForm
    context = {
        "form": form
    }
    response = loader.get_template('reservation.html')
    
    def get(self, request):
        
        return HttpResponse(self.response.render(self.context, request))
       # return render(request, "reservation.html")
    
    def post(self,request):
        form = ReservationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            reservation_year = data["reservation_start"].year
            reservation_month = data["reservation_start"].month
            reservation_day = data["reservation_start"].day
            reservation_hour = data["time"]
            reservation_minutes = data["time_minutes"]
            guests = data["guests"]

            t = dt(reservation_year, reservation_month, reservation_day, reservation_hour, reservation_minutes)
            #messages.info(request, Booking.objects.get())
            b = Booking.objects.create(
                user_id = User.objects.get([0]),
                table_id = 1,
                datetime = t
            )
            b.save()
            return HttpResponse(self.response.render(self.context, request))
        
        else:
            messages.info(request, "Nem Sikerult")
            return HttpResponse(self.response.render(self.context, request))



def bookingCreate(request):
    form = ReservationForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        reservation_year = data["reservation_start"].year
        reservation_month = data["reservation_start"].month
        reservation_day = data["reservation_start"].day
        reservation_hour = data["time"]
        reservation_minutes = data["time_minutes"]
        guests = data["guests"]

        t = dt(reservation_year, reservation_month, reservation_day, reservation_hour, reservation_minutes)
        return HttpResponse(f'Reservation Start: {t.strftime("%H:%M,%d/%m/%Y")},  {guests} Person(s)')
       
    else:
        return HttpResponse("No reservation made")
        # return HttpResponse(f'Reservation Start:{reservation_year}/{reservation_month}/{reservation_day}, {reservation_hour}:{reservation_minutes},  {guests} Person(s)')
     #   print(form.cleaned_data["reservation_start"])
    #return HttpResponseRedirect("reservation/")

'''
def  get_form(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("Thank You")
    else:
        form = ReservationForm()
    return render(request, "reservation.html", {"form": form})
'''

class Menu(View):

    def get(self, request):
        food = Food.objects.all()
        context = {
            'foods': food
            }
        return render(request, "menu.html", context=context)
