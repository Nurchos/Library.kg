from django.db import models


class ClothingCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')

    class Meta:
        verbose_name = 'Категория одежды'
        verbose_name_plural = 'Категории одежды'
        ordering = ['name']  # Сортировка по алфавиту

    def __str__(self):
        return self.name


class Clothes(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название одежды')
    price = models.FloatField(default=300, verbose_name='Цена')
    clothing_category = models.ManyToManyField(ClothingCategory, related_name="clothes")
    objects = models.Manager()

    class Meta:
        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежда'
        ordering = ['-id']  # Новые вещи будут первыми

    def __str__(self):
        return self.title
