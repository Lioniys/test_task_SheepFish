from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Site


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')


class UserSiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['name', 'url']
