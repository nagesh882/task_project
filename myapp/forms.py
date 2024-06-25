from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class signUpForm(UserCreationForm):
    password1 = forms.CharField(label='Set password',widget=forms.PasswordInput(attrs={'placeholder':'Set password', 'class':'form-control'}))
    password2 = forms.CharField(label='Confirm password(again)', widget=forms.PasswordInput(attrs={'placeholder':'confirm password', 'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username':forms.TextInput(attrs={'placeholder':'Enter username', 'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'placeholder':'Enter first name', 'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'placeholder':'Enter last name', 'class':'form-control'}),
            'email':forms.EmailInput(attrs={'placeholder':'Enter email', 'class':'form-control'}),
        }


class signInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter username', 'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Enter password", 'class':'form-control'}))
    class Meta:
        model = User