from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms

class createNewUser(UserChangeForm):
    password=forms.CharField(widget=forms.PasswordInput(),required=True)
    class Meta:
        model=User
        fields='__all__'