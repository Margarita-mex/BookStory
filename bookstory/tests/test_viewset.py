from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_204_NO_CONTENT
from rest_framework.utils import json
from snapshottest.django import TestCase
from bookstory.factories import OrderFactory, AuthorFactory
from bookstory.models import Order, Book, Author



class AuthorTest(APITestCase, TestCase):
    def setUp(self):
        self.author = AuthorFactory.create()
        self.url = reverse('api_author-list')

    def test_get_author_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertMatchSnapshot(response.json())

    def test_post_author_create(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertMatchSnapshot(response.json())

    def test_get_author_read_id(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data, {'id': 1, 'title': 'Тестовый Августин'})
        self.assertEqual(json.loads(response.content), {'id': 1, 'title': 'Тестовый Августин'})
        self.assertMatchSnapshot(response.json())

    def test_put_author_update_id(self):
        response = self.client.put(self.url, self.author)
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertMatchSnapshot(response.json())

    def test_patch_author_partial_update_id(self):
        response = self.client.patch(self.url, self.author)
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertMatchSnapshot(response.json())

    def test_delete_author_id(self):
        response = self.client.delete(self.url, self.author)
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)
        self.assertMatchSnapshot(response.json())



# class BookTest(APITestCase, TestCase):
#     def setUp(self):
#         self.author = AuthorFactory.create()
#
#     def test_create_book(self):
#         url = reverse('api_book-list')
#         data = {
#             # "author": self.author.pk,
#             "title": "test",
#             "language": "en",
#             "short_content": "hello world"
#         }
#         response = self.client.post(url, data=data)
#         self.assertEqual(response.status_code, HTTP_201_CREATED)
#         self.assertMatchSnapshot(response.json())




