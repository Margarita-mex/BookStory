from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.status import HTTP_201_CREATED
from snapshottest.django import TestCase
from bookstory.factories import OrderFactory, AuthorFactory
from bookstory.models import Order, Book, Author


class BookTest(APITestCase, TestCase):
    def setUp(self):
        self.author = AuthorFactory.create()

    def test_create_book(self):
        url = reverse('api_book-list')
        data = {
            # "author": self.author.pk,
            "title": "test",
            "language": "en",
            "short_content": "hello world"
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertMatchSnapshot(response.json())




