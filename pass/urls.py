from django import views
from django.urls import path

from . import views

app_name = 'pass'
urlpatterns = [
    path('generateRandom', views.randomGenrator),
    path('generateRandomWithLength', views.randomGenratorWithLength),
    path('generateRandomWithArguments', views.randomWithArguments),
    path('generateRandomWithMinimum', views.randomWithMinimum),
    path('generateRandomWithCustom', views.randomWithCustom),
    path('generateRandomPerfect', views.randomPerfect),
    path('generateFromString', views.fromString),
]
