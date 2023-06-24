
from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('',uradiPrvo,name='uradiPrvo' ),
    path('index', index, name='index'),
    path('termini/<str:tablice>/<str:datum>/<int:agencija>/<str:vreme>/recervacija', recervaija, name='recervacija'),
    path('termini/<str:tablice>/<str:datum>/<int:agencija>/', termini, name='termini'),
]