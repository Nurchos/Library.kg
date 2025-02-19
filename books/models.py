from django.db import models


class BooksModel(models.Model):
    GENRE_CHOICES = (
        ('COMEDY', 'Comedy'),
        ('SCIENCE', 'Science'),
        ('HORROR', 'Horror'),
        ('ROMANCE', 'Romance'),
        ('FANTASY', 'Fantasy')
    )

    objects = models.Manager()

    image = models.ImageField(upload_to='books/', verbose_name='Загрузите фото')
    title = models.CharField(max_length=120, verbose_name='Название книги')
    description = models.TextField(verbose_name='Описание книги', blank=True)
    price = models.PositiveIntegerField(verbose_name='Цена книги', default=200)
    created_at = models.DateField(auto_now_add=True)
    genre = models.CharField(max_length=10, choices=GENRE_CHOICES, default='FANTASY', verbose_name='Жанр')
    pages = models.PositiveIntegerField(verbose_name='Количество страниц', default=250)
    author = models.CharField(max_length=100, default='Чынгыз Айтматов')
    audio_book = models.URLField(verbose_name='Ссылка на аудиокнигу', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Review(models.Model):
    STARS = (
        ('🌟', '1 звезда'),
        ('🌟🌟', '2 звезды'),
        ('🌟🌟🌟', '3 звезды'),
        ('🌟🌟🌟🌟', '4 звезды'),
        ('🌟🌟🌟🌟🌟', '5 звезд'),
    )

    choice_book = models.ForeignKey(BooksModel, on_delete=models.CASCADE, related_name='reviews')
    created_at = models.DateField(auto_now_add=True)
    text_review = models.TextField(default='Крутой фильм')
    stars = models.CharField(max_length=10, choices=STARS, default='🌟🌟🌟')

    def __str__(self):
        return f'{self.stars} — {self.choice_book.title}'
