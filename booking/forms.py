from .models import Booking
from django import forms


class ReservationForm(forms.Form):

    time = forms.IntegerField(widget = forms.Select(choices=[(0, "10"), (1, "20")]))

    reservation_start = forms.DateTimeField(widget=forms.SelectDateWidget(), label="Start of Reservation")
    guests = forms.IntegerField(label="Number of Guests")