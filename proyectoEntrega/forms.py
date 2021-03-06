from tkinter.tix import Form
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','password1','password2']
        help_texts = {k:'' for k in fields}


