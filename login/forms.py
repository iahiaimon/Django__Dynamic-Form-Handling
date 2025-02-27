
from django import forms
from . import models

class LoginForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = models.User
        fields = '__all__'
        labels = {
            'name' : "Name" ,
            'pasword' : "Password",
            'image' :"Image"
        }

        help_texts = {
            'name' : "Enter your name" ,
            'pasword' : "Enter your password" ,
            'phone' : "Enter your phone number" ,
        }
