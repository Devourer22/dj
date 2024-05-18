from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Введите ваше имя')
    last_name = forms.CharField(max_length=30, required=True, help_text='Введите вашу фамилию')
    group = forms.CharField(max_length=30, required=True, help_text='Введите вашу группу')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'group', 'password1', 'password2')