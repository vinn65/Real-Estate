from dataclasses import fields
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from . models import User, property
from django import forms


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2','avatar']


class PropertyRegistrationform(forms.ModelForm):
    class Meta:
        model = property
        fields = '__all__'
        exclude = ['owner']