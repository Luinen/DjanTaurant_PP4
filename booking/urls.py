from .import views
from django.urls import path

urlpatterns = [
    path('', views.mainPage, name='main'),
    path('reservation/', views.Reservation.as_view(), name="reservation"),
    path('menu/', views.Menu.as_view(), name="menu"),
    path('reservation/makereservation/', views.bookingCreate, name="makereservation"),
]