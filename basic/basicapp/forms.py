from django import forms
from django.core import validators
from django.contrib.auth.models import User
from basicapp.models import Profile

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    email=forms.EmailField()
    text=forms.CharField(widget=forms.Textarea)

    class Meta():
        model=User
        fields=('username','email','password')

class ProfileForm(forms.ModelForm):
    class Meta():
        model = Profile
        fields=('portfolio_site','pic')