from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('', include('clothes.urls')),
    path('book_detail/<int:id>/', views.BookDetailView.as_view(), name='show_detail'),
    path('about_me/', views.AboutMeView.as_view(), name='about_me'),
    path('photo/', views.PhotoView.as_view(), name='photo'),
    path('time/', views.TimeView.as_view(), name='time'),
    path('search/', views.SearchView.as_view(), name='search'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
