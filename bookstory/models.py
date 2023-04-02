from datetime import datetime
from django.db import models


class Author(models.Model):
    title = models.CharField('Имя автора', max_length=100)
    language = models.CharField('Язык', max_length=20)
    bio = models.TextField('Биография')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


# Create your models here.
class Book(models.Model):
    title = models.CharField('Название', max_length=100)
    language = models.CharField('Язык', max_length=20)
    short_content = models.TextField('Краткое описание')
    author = models.ManyToManyField('Author', related_name='book')
    cost = models.DecimalField('Цена', decimal_places=2, max_digits=6, default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Order(models.Model):
    book = models.ManyToManyField('Book', related_name='book')
    title = models.CharField('Имя', max_length=100)
    phone = models.CharField('Номер телефона', max_length=11)
    date_and_time = models.DateTimeField('дата заказа', default=datetime.now())

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
