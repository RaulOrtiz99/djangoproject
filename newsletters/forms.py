from dataclasses import fields
from pyexpat import model
from django import forms
from .models import NewsLetterUser,NewsLetter


class NewsletterUserSignUpForm(forms.ModelForm): #esto es para el backend  para llenar los emails 
    class meta:
        model = NewsLetterUser
        fields = ['email']

class NewsletterCreationForm(forms.ModelForm): #esto es para crear o mas bien llenar un correo 
    class Meta:
        model = NewsLetter
        fields = ['name','subject','body','email']