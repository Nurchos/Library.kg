from django.urls import path
from . import views

app_name = 'recipe'

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/add/', views.add_recipe, name='add_recipe'),
    path('recipe/<int:pk>/ingredient/add/', views.add_ingredient, name='add_ingredient'),
    path('recipe/<int:pk>/delete/', views.delete_recipe, name='delete_recipe'),
]
