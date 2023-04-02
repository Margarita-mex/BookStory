from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bookstory.views import BookViewSet

router = DefaultRouter()
router.register('book', BookViewSet, 'api_book')

urlpatterns = [
    path('api', include(router.urls))
]