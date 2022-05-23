from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

#from django.conf import settings

class Resume(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100, verbose_name="Имя")   # Имя
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")    #Фамилия
    age = models.IntegerField(verbose_name="Возраст")   #Возраст
    field_of_activity = models.CharField(max_length=50, verbose_name="Сфера деятельности")  #Сфера деятельности
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True, verbose_name="Фото")
    text = models.TextField(verbose_name="Расскажите о себе")      #Поле для вода информации о себе
    load_date = models.DateTimeField(auto_now=True)     #Время загрузки резюме
    user_resume = models.ForeignKey('Users', models.SET_NULL, blank=True, null=True)

    
    def __str__(self):
        return self.id
    
    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'


class Contacts(models.Model):
    mobile = models.IntegerField()
    sity = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    cont = models.ForeignKey('Contacts', on_delete=models.PROTECT, null=True)


    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class Users(AbstractUser):  
    email = models.EmailField()
    sity = models.CharField(max_length=50)
    #resum = models.ForeignKey('Resume', on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True, verbose_name="Фото_Пользователя", null=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'


# class Edit_Resume(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.EmailField()
    