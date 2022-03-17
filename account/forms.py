#from django.contrib.auth.models import Resume
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic.edit import CreateView
from my_site.models import Users
#from django.forms import widgets
#from my_site.models import Resume


# class LoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин',widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = Users
        fields = ('username', 'password1','password2')
        widget = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
        }
    
    
    #Здесь будет форма для edit_resume

class Edit_Forms(forms.Form):
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input'}))
    sity = forms.CharField(label='Город проживания', widget=forms.TextInput(attrs={'class': 'form-input'}))
    photo = forms.ImageField(required = False)


    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'sity', 'photo')

    # class Meta:
    #     model = Resume
    #     fields = ('first_name', 'last_name')

    # def clean_password2(self):
    #     cd = self.cleaned_data
    #     if cd['password'] != cd['password2']:
    #         raise forms.ValidationError('Пароли не совпадают')
    #     return cd['password2']


