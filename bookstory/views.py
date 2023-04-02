from bookstory.models import Author, Book, Order
from bookstory.serializers import AuthorSerializer, BookSerializer, OrderSerializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet


class AuthorViewSet(ModelViewSet, GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(ModelViewSet, GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class OrderViewSet(ModelViewSet, GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
