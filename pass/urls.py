from django import views
from django.urls import path

from . import views

app_name = 'pass'
urlpatterns = [
    path('test', views.test),
]
