from .models import Booking
from django import forms


class ReservationForm(forms.Form):
    reservation_start = forms.DateTimeField(label="Start of Reservation")
    guests = forms.IntegerField(label="Number of Guests")