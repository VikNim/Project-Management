from django import forms
from .models import UserInfo


class LoginForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['username', 'password']
        widgets = {'password': forms.PasswordInput()}


class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'position']
        widgets = {'password': forms.PasswordInput()}
