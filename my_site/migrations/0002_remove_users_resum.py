# Generated by Django 3.2.9 on 2022-04-30 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='resum',
        ),
    ]
