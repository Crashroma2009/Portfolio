from django.test import TestCase
from .models import Users, Resume, Contacts
from model_bakery import baker


class TestModelsUsers(TestCase):
    """Тестирование модели User"""

    # @classmethod
    # def setUpTestData(cls):
    #     Users.objects.create(email='info2009@mail.com')


    def test_model_email(self):
        #user = Users.objects.get(id=1)
        user = Users(email='info2009', sity='Rostov')
        user.save()
        self.assertEquals(user.email, 'info2009', 'Ошибка знаения БД')
        self.assertEquals(user.sity, 'Rostov', 'Ошибка знаения БД' )
        #field_label = user._meta.get_field('email').verbose_name
        #self.assertEquals(field_label, 'email')


class TestModelResume(TestCase):
    """Тестирование модели Resume"""

    def create_resume(self):
        return Resume.objects.create(first_name='Рома', last_name='Дейнега',
                                    age='21', field_of_activity='Строитель')

    
    def test_resume(self):
        resume = self.create_resume()
        self.assertEquals(resume.first_name, 'Рома', 'Ошибка знаения БД')
        self.assertEquals(resume.last_name, 'Дейнега', 'Ошибка знаения БД')
        self.assertEquals(resume.age, '21', 'Ошибка знаения БД')
        self.assertEquals(resume.field_of_activity, 'Строитель', 'Ошибка знаения БД')


class TestModelsContacts(TestCase):
    """Тестирование модели Contacts"""

    def create_contacts(self):
        return Contacts.objects.create(mobile='89686255581',
                                        sity='Rostov',
                                        email='info2009')


    def test_contacts(self):
        contacts = self.create_contacts()
        self.assertEquals(contacts.mobile, '89686255581')
        self.assertEquals(contacts.sity, 'Rostov')
        self.assertEquals(contacts.email, 'info2009')


    # def test_contacts(self):
    #     mobile = baker.make(Contacts, mobile='89686255581')
    #     sity = baker.make(Contacts, sity='Rostov')
    #     email = baker.make(Contacts, email='info2009')    
    #     self.assertEquals(mobile, '89686255581')
    #     self.assertEquals(sity, 'Rostov')
    #     self.assertEquals(email, 'info2009')