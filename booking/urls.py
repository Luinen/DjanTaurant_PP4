from .import views
from django.urls import path

urlpatterns = [
    path('', views.mainPage, name='main'),
    path('reservation/', views.Reservation.as_view(), name="reservation"),
    path('menu/', views.Menu.as_view(), name="menu"),
    path('showbookings/', views.Mybookings.as_view(), name="mybookings"),
    path('showbookings/delete/<int:day>/<int:month>/<int:year>/<int:hour>/<int:min>', views.Deletebooking.as_view(), name='deletebooking'),
    path('showbookings/update/<int:day>/<int:month>/<int:year>/<int:hour>/<int:min>', views.Updatebooking.as_view(), name='updatebooking')
]