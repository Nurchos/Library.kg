from datetime import datetime
from django.views import View
from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from django.views import generic


class BookListView(ListView):
    model = models.BooksModel
    template_name = 'show.html'
    context_object_name = 'books'
    ordering = ['-id']


class SearchView(generic.ListView):
    template_name = 'show.html'
    context_object_name = 'books'

    def get_queryset(self):
        query = self.request.GET.get('q', '').strip()
        if query:
            return models.BooksModel.objects.filter(title__icontains=query)
        return models.BooksModel.objects.none()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context


class BookDetailView(View):
    def get(self, request, id):
        form = forms.ReviewForm()
        book = get_object_or_404(models.BooksModel, id=id)
        context = {'book': book, 'form': form}
        return render(request, 'show_detail.html', context)

    def post(self, request, id):
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.choice_book = get_object_or_404(models.BooksModel, id=id)
            review.save()
            return redirect('show_detail', id=id)
        return HttpResponse("Форма не валидна")



class AboutMeView(View):
    def get(self, request):
        return HttpResponse(
            'Здравствуйте! Добро пожаловать на мой веб-сайт.) Меня зовут Нурмухаммед и я люблю слушать музыку.'
        )


class PhotoView(View):
    def get(self, request):
        return HttpResponse("<img src='https://i1.sndcdn.com/artworks-g2OSrF3ZutlznKbX-XuNR5g-t500x500.jpg' />")


class TimeView(View):
    def get(self, request):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return HttpResponse(f"<h1>Текущее время:</h1><p>{now}</p>")
