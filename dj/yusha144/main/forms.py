# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.forms import TextInput, Select, PasswordInput


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'group', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'id': 'username',
                'name': 'username'
            }),
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'id': 'first_name',
                'name': 'first_name'
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'id': 'last_name',
                'name': 'last_name'
            }),
            'group': Select(attrs={
                'class': 'form-control',
                'id': 'group',
                'name': 'group'
            }),
            'password1': PasswordInput(attrs={
                'class': 'form-control',
                'id': 'password1',
                'name': 'password1'
            }),
            'password2': PasswordInput(attrs={
                'class': 'form-control',
                'id': 'password2',
                'name': 'password2'
            }),
        }


# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'id': 'id_username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'id': 'id_password'})
