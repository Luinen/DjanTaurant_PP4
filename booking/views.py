from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.template import loader
from django import forms
from .forms import ReservationForm
from datetime import datetime as dt
from datetime import timedelta
from booking.models import Food, Capacity, Booking
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse

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
            restaurant_name = 'Djantaurant'
            restaurant = Capacity.objects.filter(name = restaurant_name)[0]
            user = User.objects.filter(username=request.user)[0]

            t = dt(reservation_year, reservation_month, reservation_day, reservation_hour, reservation_minutes)
            res_ontime = Booking.objects.filter(datetime__range= [t - timedelta(hours=2), t])
            #res_ontime = Booking.objects.filter(datetime__range=[t, t + timedelta(hours=2)])
            print(res_ontime)
            if t < dt.now():
                messages.info(request, "Nem Sikeres a foglalas")
                return HttpResponseRedirect("/reservation")
            if not request.user.is_authenticated:
                messages.info(request, "Bejelentkezes szukseges")
                return HttpResponseRedirect("/reservation")
            total = 0
            for i in res_ontime:
                total += i.guest_number
            if (total + guests) > restaurant.capacity:
                messages.info(request, "Tul sokan vannak")
                return HttpResponseRedirect("/reservation")
            #messages.info(request, Booking.objects.get())
            b = Booking.objects.create(
                user= user,
                restaurant= restaurant,
                datetime= t,
                guest_number= guests
            )
            b.save()
            print(User.objects.all()[0])
            messages.info(request, "Sikeres foglalas")
            return HttpResponseRedirect("/reservation")
        
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

class Menu(View):

    def get(self, request):
        response = loader.get_template('index.html')
        food = Food.objects.all()
        context = {
            'foods': food
        }
        return HttpResponse(response.render(context, request))

class Mybookings(View):

    def get(self, request):
        if request.user.is_superuser:
            response = loader.get_template('mybooking.html')
            booking = Booking.objects.all()
            context = {
                'bookings': booking
            }
            return HttpResponse(response.render(context, request))
        elif request.user.is_authenticated:
            response = loader.get_template('mybooking.html')
            booking = Booking.objects.filter(user=request.user)
            context = {
                'bookings': booking
            }
            return HttpResponse(response.render(context, request))



class Deletebooking(View):

    def get(self, request, day, month, year, hour, min):
        if request.user.is_authenticated:
            bookingdt = dt(year=year, month=month, day=day, hour=hour, minute=min)
            Booking.objects.filter(user=request.user, datetime=bookingdt).delete()
            return HttpResponseRedirect(reverse('mybookings'))