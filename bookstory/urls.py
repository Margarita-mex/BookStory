from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bookstory.views import BookViewSet, OrderViewSet, AuthorViewSet

router = DefaultRouter()
router.register('author', AuthorViewSet, 'api_author')
router.register('book', BookViewSet, 'api_book')
router.register('order', OrderViewSet, 'api_order')

urlpatterns = [
    path('api', include(router.urls))
]