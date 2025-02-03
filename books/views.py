from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def about_me(request):
    if request.method == 'GET':
        return HttpResponse(
            'Здравствуйте! Добро пожаловать на мой веб-сайт.) Меня зовут Нурмухаммед и я люблю слушать музыку.')


def photo(request):
    if request.method == 'GET':
        return HttpResponse("<img src='https://i1.sndcdn.com/artworks-g2OSrF3ZutlznKbX-XuNR5g-t500x500.jpg' />")


def time(request):
    if request.method == 'GET':
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return HttpResponse(f"<h1>Текущее время:</h1><p>{now}</p>")
