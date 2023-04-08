from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_204_NO_CONTENT
from rest_framework.utils import json
from snapshottest.django import TestCase
from bookstory.factories import OrderFactory, AuthorFactory
from bookstory.models import Order, Book, Author



class AuthorTest(APITestCase, TestCase):
    def setUp(self):
        self.author = AuthorFactory()
        self.url = reverse('api_author-list')

    def test_get_author_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertMatchSnapshot(response.json())

    def test_post_author_create(self):
        data ={
            'title' : 'Тестовый Августин',
            'language' : 'русский',
            'bio' :'пишет часто по осени',
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertMatchSnapshot(response.json())

    def test_put_author_update_id(self):
        data = {
             'title': 'Тестовый Августин',
             'language': 'русский',
             'bio': 'пишет часто по осени',
             'id': 1,
        }
        url = reverse('api_author-detail', kwargs={'pk': self.author.pk})
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertMatchSnapshot(response.json())

    def test_patch_author_partial_update_id(self):
        data = {
            'title': 'Тестовый Августин',
            'language': 'русский',
            'bio': 'пишет часто по осени',
            'id': 1,
        }
        url = reverse('api_author-detail', kwargs={'pk': self.author.pk})
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertMatchSnapshot(response.json())

    def test_delete_author_id(self):
        data = {
            'title': 'Тестовый Августин',
            'language': 'русский',
            'bio': 'пишет часто по осени',
            'id': 1,
        }
        url = reverse('api_author-detail', kwargs={'pk': self.author.pk})
        response = self.client.delete(url, data)
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)


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




