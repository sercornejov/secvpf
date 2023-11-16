from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Geninfo

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

class GeninfoForm(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = Geninfo
		fields = ['firstname', 'lastname','profession','birthday','introphrase','introtext','logo','photo','user']