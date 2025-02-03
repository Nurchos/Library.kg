from django.urls import path
from . import views

urlpatterns = [
    path('about_me/', views.about_me, name='about_me'),
    path('photo/', views.photo, name='photo'),
    path('time/', views.time, name='time')
]
