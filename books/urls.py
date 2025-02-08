from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list_view, name='book_list'),
    path('book_detail/<int:id>/', views.book_detail_view, name='film_detail'),

    path('about_me/', views.about_me, name='about_me'),
    path('photo/', views.photo, name='photo'),
    path('time/', views.time, name='time')
]
