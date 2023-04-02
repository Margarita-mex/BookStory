from rest_framework.serializers import ModelSerializer

from bookstory.models import Author, Book, Order


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(ModelSerializer):
    author = AuthorSerializer(many=True, source='author_set', required=False)

    class Meta:
        model = Book
        fields = "__all__"


class OrderSerializer(ModelSerializer):
    book = BookSerializer(many=True, source='book_set')

    class Meta:
        model = Order
        fields = "__all__"
