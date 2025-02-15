from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.book_list_view, name='book_list'),
    path('', include('clothes.urls')),
    path('book_detail/<int:id>/', views.book_detail_view, name='book_detail'),

    path('about_me/', views.about_me, name='about_me'),
    path('photo/', views.photo, name='photo'),
    path('time/', views.time, name='time')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
