from django.views.generic import ListView
from .models import Clothes


class AllClothesListView(ListView):
    model = Clothes
    template_name = 'clothes/all_clothes.html'
    context_object_name = 'all_clothes'
    ordering = ['-id']


class BabyClothesListView(ListView):
    model = Clothes
    template_name = 'clothes/baby.html'
    context_object_name = 'baby'

    def get_queryset(self):
        return Clothes.objects.filter(clothing_category__name='для детей').order_by('-id')


class TeenClothesListView(ListView):
    model = Clothes
    template_name = 'clothes/teenage.html'
    context_object_name = 'teenage'

    def get_queryset(self):
        return Clothes.objects.filter(clothing_category__name='для подростков').order_by('-id')


class AdultClothesListView(ListView):
    model = Clothes
    template_name = 'clothes/adult.html'
    context_object_name = 'adult'

    def get_queryset(self):
        return Clothes.objects.filter(clothing_category__name='для взрослых').order_by('-id')
