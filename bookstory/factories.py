import factory
from datetime import datetime

from bookstory.models import Author, Book, Order


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    title = 'Тестовый Августин'
    language = 'русский'
    bio = 'пишет часто по осени'


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = 'Осенние рассказы'
    language = 'русский'
    short_content = 'про листья на земле'
    cost = '500'

    @factory.post_generation
    def authors(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for author in extracted:
                self.authors.add(author)


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

    title = 'Александр'
    phone = '+7 666 666 66 66'
    date_and_time = datetime(2022, 8, 25, 7, 30)

    @factory.post_generation
    def books(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for book in extracted:
                self.books.add(book)
