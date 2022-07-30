from django import views
from django.urls import path

from . import views

app_name = 'pass'
urlpatterns = [
    path('genrateRandom', views.randomGenrator),
    path('genrateRandomWithLength', views.randomGenratorWithLength),
]
