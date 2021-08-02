from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('signup',views.signup, name='signup'),
    path('login',views.login, name='login'),
    path('updateprofile', views.updateprofile, name='updateprofile'),
    path('mycar', views.mycar, name='mycar'),
    path('bookings', views.bookings, name='bookings'),
    path('changepass', views.changepass, name='changepass'),
    path('addcar', views.addcar, name='addcar'),
    path('bookcar', views.bookcar, name='bookcar'),
    path('rentcar', views.rentcar, name='rentcar')


]

