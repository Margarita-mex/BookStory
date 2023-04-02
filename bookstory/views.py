from bookstory.models import Author, Book, Order
from bookstory.serializers import AuthorSerializer, BookSerializer, OrderSerializer
from rest_framework.viewsets import ModelViewSet


class AuthorViewSet(ModelViewSet):
    queryset = Author.object.all()
    serializer_class = AuthorSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.object.all()
    serializer_class = BookSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.object.all()
    serializer_class = OrderSerializer
