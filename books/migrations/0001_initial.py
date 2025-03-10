# Generated by Django 5.1.5 on 2025-02-07 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BooksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='books/', verbose_name='загрузите фото')),
                ('title', models.CharField(max_length=120, verbose_name='укажите название книги')),
                ('description', models.TextField(blank=True, verbose_name='укажите описание фильма')),
                ('price', models.PositiveIntegerField(default=200, verbose_name='укажите цену книги')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('genre', models.CharField(choices=[('COMEDY', 'COMEDY'), ('SCIENCE', 'SCIENCE'), ('HORROR', 'HORROR'), ('ROMANCE', 'ROMANCE'), ('FANTASY', 'FANTASY')], default='FANTASY', max_length=10, verbose_name='выберите жанр')),
                ('pages', models.PositiveIntegerField(default=250, verbose_name='укажите количество страниц')),
                ('author', models.CharField(default='Чынгыз Айтматов', max_length=100)),
                ('audio_book', models.URLField(verbose_name='укажите ссылку из YOUTUBE')),
            ],
        ),
    ]
