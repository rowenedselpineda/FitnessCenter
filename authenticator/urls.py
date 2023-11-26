from django.urls import path, include
from authenticator import views

urlpatterns = [
    path('', views.home, name='Home'),

]
