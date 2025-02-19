from django.urls import path
from .views import AllClothesListView, BabyClothesListView, TeenClothesListView, AdultClothesListView

urlpatterns = [
    path('all_clothes/', AllClothesListView.as_view(), name='all_clothes'),
    path('baby_clothes/', BabyClothesListView.as_view(), name='baby_clothes'),
    path('teen_clothes/', TeenClothesListView.as_view(), name='teen_clothes'),
    path('adult_clothing/', AdultClothesListView.as_view(), name='adult_clothing'),
]
