import datetime
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from . import models, forms


def book_list_view(request):
    if request.method == 'GET':
        query = models.BooksModel.objects.all().order_by('-id')
        context_object_name = {
            'book': query,
        }
        return render(request, template_name='show.html',
                      context=context_object_name)


def book_detail_view(request, id):
    if request.method == "GET":
        form = forms.ReviwForm()
        query = get_object_or_404(models.BooksModel, id=id)
        context_object_name = {
            'book_id': query,
            'form': form
        }
        return render(request, template_name='show_detail.html',
                      context=context_object_name)
    elif request.method == "POST":
        form = forms.ReviwForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.choice_book = get_object_or_404(models.BooksModel, id=id)
            review.save()
            return redirect('show_detail', id=id)
        else:
            return HttpResponse("Форма не валидна")


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
