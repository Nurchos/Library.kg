from django.shortcuts import render
from . import models
from .models import Clothes  # noqa


def all_clothes(request):
    if request.method == "GET":
        query = models.Clothes.objects.all().order_by('-id')
        context_object_name = {
            'all_clothes': query
        }
        return render(request, template_name='clothes/all_clothes.html',
                      context=context_object_name)


def baby_clothes(request):
    if request.method == "GET":
        query = models.Clothes.objects.filter(clothing_category__name='для детей').order_by('-id')
        context_object_name = {
            'baby': query
        }
        return render(request, template_name='clothes/baby.html',
                      context=context_object_name)


def teen_clothes(request):
    if request.method == "GET":
        query = models.Clothes.objects.filter(clothing_category__name='для подростков').order_by('-id')
        context_object_name = {
            'teenage': query
        }
        return render(request, template_name='clothes/teenage.html',
                      context=context_object_name)


def adult_clothes(request):
    if request.method == "GET":
        query = models.Clothes.objects.filter(clothing_category__name='для взрослых').order_by('-id')
        context_object_name = {
            'adult': query
        }
        return render(request, template_name='clothes/adult.html',
                      context=context_object_name)
