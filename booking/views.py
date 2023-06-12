from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.template import loader
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
            res_ontime = Booking.objects.filter(datetime__range= [t - timedelta(hours=2), t + timedelta(hours=2)])
            print(res_ontime)
            if t < dt.now():
                messages.info(request, "The reservation date is wrong.")
                return HttpResponseRedirect("/reservation")
            if not request.user.is_authenticated:
                messages.info(request, "Please log in")
                return HttpResponseRedirect("/reservation")
            total = 0
            for i in res_ontime:
                total += i.guest_number
            if (total + guests) > restaurant.capacity:
                messages.info(request, "Not enough seat for your reservation.")
                return HttpResponseRedirect("/reservation")
            b = Booking.objects.create(
                user= user,
                restaurant= restaurant,
                datetime= t,
                guest_number= guests
            )
            b.save()
            print(User.objects.all()[0])
            messages.info(request, "Successful booking.")
            return HttpResponseRedirect("/reservation")
        
        else:
            messages.info(request, "Oops, something is wrong")
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
            order = request.GET.get("order_by")
            if order == "user":
                booking = Booking.objects.all().order_by("user")
            else:
                booking = Booking.objects.all().order_by("datetime")
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


class Updatebooking(View):

    def get(self, request, day, month, year, hour, min):
        if request.user.is_authenticated:
            bookingdt = dt(year=year, month=month, day=day, hour=hour, minute=min)
            field = request.GET.get("field")
            new_value = request.GET.get("new_value")
            #print(field)
            #print(new_value)
            #print('//////////////////')
            if field == "guest_number":
                o = Booking.objects.filter(user=request.user, datetime=bookingdt)[0]
                o.guest_number = int(new_value)
                o.save()
                #print('UPDATED GUEST NUMBER')
                #print(o)
            messages.info(request, f"Reservation updated. {bookingdt.strftime('%H:%M, %d/%m/%Y')}")
            return HttpResponseRedirect(reverse('mybookings'))


class Deletebooking(View):

    def get(self, request, day, month, year, hour, min):
        if request.user.is_authenticated:
            bookingdt = dt(year=year, month=month, day=day, hour=hour, minute=min)
            if request.user.is_superuser:
                user = User.objects.filter(username= request.GET.get("user"))[0]
            else:
                user = request.user
            Booking.objects.filter(user= user, datetime=bookingdt).delete()
            messages.info(request, f"Reservation deleted. {bookingdt.strftime('%H:%M, %d/%m/%Y')}")
            return HttpResponseRedirect(reverse('mybookings'))

