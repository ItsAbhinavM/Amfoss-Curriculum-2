from django import forms
from .models import ToDoItem
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User

class ToDoItemForm(forms.ModelForm):
    class Meta:
        model=ToDoItem
        fields= ['title', 'description']

class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1', 'password2']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
