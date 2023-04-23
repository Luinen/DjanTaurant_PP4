from .import views
from django.urls import path
from .views import GenericView

urlpatterns = [
    path('', GenericView, name= 'home'),
]