from django import forms
from blog.models import Question, Profile, Answer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class AskForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text']

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
