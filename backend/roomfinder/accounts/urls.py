from django.urls import path, include
from accounts import views

urlpatterns=[
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),


]