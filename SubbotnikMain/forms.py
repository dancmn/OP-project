from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import UserAccount, Marker


class SignupForm(UserCreationForm):
    name = forms.CharField(label="Ваше имя")
    class Meta:
        model = UserAccount
        fields = ['name', 'password1', 'password2']


class MarkerForm(forms.ModelForm):
    markerName = forms.CharField(label="Название локации")
    description = forms.CharField(label="Описание", widget=forms.Textarea)
    photo = forms.ImageField(label="Фотография мусора")
    latitude = forms.CharField(label="широта")
    longitude = forms.CharField(label="долгота")

    class Meta:
        model = Marker
        fields = ['markerName',
                  'description',
                  'photo',
                  'latitude',
                  'longitude',
                  ]


class LoginForm(forms.Form):
    username = forms.CharField(label="Имя пользователя")
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
