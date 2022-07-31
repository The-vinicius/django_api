from rest_framework import routers
from .views import hello_world
from django.urls import path

urlpatterns = [
    path('hello/', hello_world, name='hello')
]
