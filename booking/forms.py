from django import forms


class ReservationForm(forms.Form):

    open_hours = [(i,f"{i}")for i in range(14, 21)]
    minutes = [(i,f"{i}")for i in range(0,60,15)]
    time = forms.IntegerField(widget = forms.Select(choices= open_hours))
    time_minutes= forms.IntegerField(widget = forms.Select(choices= minutes), label="T")

    reservation_start = forms.DateTimeField(widget=forms.SelectDateWidget(), label="Start of Reservation")
    guests = forms.IntegerField(label="Number of Guests")


class ReservationDeleteForm(forms.Form):

    time = forms.DateTimeField()