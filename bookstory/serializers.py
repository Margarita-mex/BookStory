from rest_framework.serializers import ModelSerializer

from bookstory.models import Author, Book, Order


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author


class BookSerializer(ModelSerializer):
    author = AuthorSerializer(many=True, source='author_set')

    class Meta:
        model = Book


class OrderSerializer(ModelSerializer):
    book = BookSerializer(many=True, source='book_set')

    class Meta:
        model = Order
