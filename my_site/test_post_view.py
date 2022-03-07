from django.test import TestCase
from .models import Contacts
from django.test import Client

# class TestPostContacts(TestCase):
#     """Тестирование POST запроса"""

#     def setUp(self):
#         self.client = Client()

#     def test_post_contacts(self):
#         data = {
#             'mobile': '89686255581',
#             'sity': 'Rostov',
#             'email': 'info2009@mail.com',
#         }

#         response = self.client.post('/account/edit_resume/', data=data)
#         self.assertEquals(Contacts.objects.count(), 1)
#         self.assertEquals(response, '/account/user_home/')