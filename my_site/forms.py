from django import forms
#from django.forms import widgets
from my_site.models import *
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import Users

class Resume_form(forms.ModelForm):
    #delete = forms.Input
    class Meta:
        model = Resume
        fields = ['first_name', 'last_name', 'age',  'field_of_activity', 'photo', 'text']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            #'photo': forms.ImageField(required = False),
            'text': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
        }


class Contacts_form(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['mobile', 'sity', 'email']
        widgets = {
            'mobile': forms.NumberInput(attrs={'class': 'number-input'}),
            'sity': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.TextInput(attrs={'class': 'form-input'}),
        }







