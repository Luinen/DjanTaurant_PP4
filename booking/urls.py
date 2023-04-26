from .import views
from django.urls import path
from .views import mainPage, Reservation

urlpatterns = [
    path('', mainPage, name= 'main'),
    path('reservation/', views.Reservation.as_view(), name="reservation"),
]