from django.shortcuts import render
from .forms import NewsletterUserSignUpForm
# Estas son las vistas para que los usuarios se suscriban y reciban nuestros emails 

def newsletter_signup(request):
    form = NewsletterUserSignUpForm(request.POST or None) #esto es para jalar los datos
