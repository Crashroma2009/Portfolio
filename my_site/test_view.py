#from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.http import HttpResponse
from django.test import Client, TestCase
from my_site.views import IndexHome
from .models import Users
import unittest
#import pytest
from urllib import response


# Create your tests here.

"""Проверка статуса ответа страниц"""

# @pytest.mark.parametrize('link', ['//127.0.0.1:8000/account/login/', 
#                                 '//127.0.0.1:8000/about/', 
#                                 '//127.0.0.1:8000/additional_information/',
#                                 '//127.0.0.1:8000/account/register/'])
# def test_index(link):
#     c = Client()
#     response = c.get(link)
#     assert response.status_code == 200, 'Страница не отвечает'

# if __name__ == '__main__':
#     pytest.test_index


class StatusCodeTest(unittest.TestCase):
    """Проверка ответа всех страниц status_code'. """
    def setUp(self):
        self.client = Client()

    
    def test_index(self):
        response = self.client.get('//127.0.0.1:8000/')
        self.assertEqual(response.status_code, 200, 'Не был полуен ответ от сайта')


    # def test_about(self):
    #     '''Нужно авторизаваться сначала'''
    #     response = self.client.get('//127.0.0.1:8000/about')
    #     self.assertEqual(response.status_code, 200, 'Не был полуен ответ от сайта')


    def test_additional_information(self):
        response = self.client.get('//127.0.0.1:8000/additional_information/')
        self.assertEqual(response.status_code, 200, 'Не был полуен ответ от сайта')


    def test_account_register(self):
        response = self.client.get('//127.0.0.1:8000/account/register/')
        self.assertEqual(response.status_code, 200, 'Не был полуен ответ от сайта')


    def test_account_login(self):
        response = self.client.get('//127.0.0.1:8000/account/login/')
        self.assertEqual(response.status_code, 200, 'Не был полуен ответ от сайта')


    # def test_template(self):
    #     response = self.client.get('//127.0.0.1:8000/')
    #     self.assertTemplateUsed(response, index, f'Другой шаблон пришел {response}')

    # class BaseModelTest(unittest.TestCase):
    #     """Тесты на запросы в базу данных"""
    #     def setUp(self):
    #         self.client = Client() 
    #         # self.user = Users.objects.create(email='user@mail.com', sity='Rostov')
    #         # image = SimpleUploadedFile("photo.jpg", content=b'', content_type="image/jpg")
    #         self.user = Users()


#         def test_add_user(self):
#             pass