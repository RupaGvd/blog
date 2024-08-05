from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class Signupform(UserCreationForm):
    password2 = forms.CharField(widget=forms.PasswordInput(),label='Retype-Password')
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        lables = {'username':'User Name','first_name':'First Name','last_name':'Last Name','email':'Email Address'}
        widget  = {'username':forms.TextInput(attrs={'blank':True})}
