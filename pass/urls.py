from django import views
from django.urls import path

from . import views

app_name = 'pass'
urlpatterns = [
    path('generateRandom', views.randomGenrator),
    path('generateRandomWithLength', views.randomGenratorWithLength),
    path('generateRandomWithArguments', views.randomWithArguments),
]
