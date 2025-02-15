from django.db import models


class BooksModel(models.Model):
    GENRE_CHOICES = (
        ('COMEDY', 'COMEDY'),
        ('SCIENCE', 'SCIENCE'),
        ('HORROR', 'HORROR'),
        ('ROMANCE', 'ROMANCE'),
        ('FANTASY', 'FANTASY')
    )
    objects = models.Manager
    image = models.ImageField(upload_to='books/', verbose_name='загрузите фото')
    title = models.CharField(max_length=120, verbose_name='укажите название книги')
    description = models.TextField(verbose_name='укажите описание фильма', blank=True)
    price = models.PositiveIntegerField(verbose_name='укажите цену книги', default=200)
    created_at = models.DateField(auto_now_add=True)
    genre = models.CharField(max_length=10, choices=GENRE_CHOICES, default='FANTASY', verbose_name='выберите жанр')
    pages = models.PositiveIntegerField(verbose_name='укажите количество страниц', default=250)
    author = models.CharField(max_length=100, default='Чынгыз Айтматов')
    audio_book = models.URLField(verbose_name='укажите ссылку из YOUTUBE')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'


class Review(models.Model):
    STARS = (
        ('🌟', '🌟'),
        ('🌟🌟', '🌟🌟'),
        ('🌟🌟🌟', '🌟🌟🌟'),
        ('🌟🌟🌟🌟', '🌟🌟🌟🌟'),
        ('🌟🌟🌟🌟🌟', '🌟🌟🌟🌟🌟'),
    )
    choice_book = models.ForeignKey(BooksModel, on_delete=models.CASCADE,
                                    related_name='choice_book')
    created_at = models.DateField(auto_now_add=True)

    text_review = models.TextField(default='Крутой фильм')
    stars = models.CharField(max_length=10, choices=STARS, default='🌟🌟🌟')

    def __str__(self):
        return f'{self.stars}--{self.choice_book.title}'
