from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post

class Signupform(UserCreationForm):
    password2 = forms.CharField(widget=forms.PasswordInput(),label='Retype-Password')
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'username':'User Name','first_name':'First Name','last_name':'Last Name','email':'Email Address'}

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        