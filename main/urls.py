from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.redirect),
    path('admin/', admin.site.urls),
    path('pass/', include('pass.urls')),
]
