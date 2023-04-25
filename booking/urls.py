from .import views
from django.urls import path
from .views import mainPage, signUp

urlpatterns = [
    path('', mainPage, name= 'main'),
    path('sign_up/', signUp, name= 'sign_up')
]