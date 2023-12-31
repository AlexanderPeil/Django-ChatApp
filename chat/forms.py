from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


"""
    Custom sign-up form extending UserCreationForm to include an email field.
"""
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')