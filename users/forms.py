<<<<<<< HEAD
<<<<<<< HEAD
from dataclasses import fields
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
=======
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
>>>>>>> da3582c0a317addf7b9646b91452defa9e38b670
=======
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
>>>>>>> da3582c0a317addf7b9646b91452defa9e38b670
from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "autofocus": True,
        'class': 'form-control',
        'placeholder': "Input username"
        }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password",
            'class': "form-control",
            'placeholder': "Input password",
            }),
    )
    class Meta:
        model = User
        fields = ['username', 'password',] 


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = {
            "first_name",
            "last_name",
            "username",
<<<<<<< HEAD
<<<<<<< HEAD
            'email',
=======
>>>>>>> da3582c0a317addf7b9646b91452defa9e38b670
=======
>>>>>>> da3582c0a317addf7b9646b91452defa9e38b670
            "password1",
            "password2",
        }

    first_name = forms.CharField()        
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()        
    password2 = forms.CharField()
<<<<<<< HEAD
<<<<<<< HEAD

class UserProfileForm(UserChangeForm):

    class Meta:
        model = User()
        fields = {
            'image',
            'first_name',
            'last_name',
            'username',
            'email',
        }
    image = forms.ImageField(required=False)
    first_name = forms.CharField()        
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    
=======
>>>>>>> da3582c0a317addf7b9646b91452defa9e38b670
=======
>>>>>>> da3582c0a317addf7b9646b91452defa9e38b670
        