from django import forms
from blog.models import Question, Profile, Answer, Tag
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import SelectMultiple

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class AskForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text', 'tags']
        widgets = {
            'tags': SelectMultiple(),
        }

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text']

class SettingsForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    avatar = forms.ImageField(required=False)

class TagForm(forms.Form):
    tag = forms.CharField()