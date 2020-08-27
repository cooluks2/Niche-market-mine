from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class SingupForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'required': 'True',
        }
    ))


    class Meta:
        model = User
        fields = ("username","email","first_name","last_name", "password1", "password2",)

