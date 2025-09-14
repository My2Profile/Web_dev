from django import forms
from .models import Genre
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class GenreForm(forms.ModelForm): 
	class Meta:
		model = Genre
		fields = ['name', 'description']



class LoginForm(forms.Form):

	username = forms.CharField(max_length=50)
	password = forms.CharField(max_length=50)



class RegisterForm(UserCreationForm):

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

