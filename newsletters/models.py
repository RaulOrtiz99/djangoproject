import email
from django.db import models

# Create your models here.

#Estos son los modelos del usuario

class NewsLetterUser(models.Model): #este es el modelo para el usuario
    email = models.EmailField(null=False, unique=True)
    date_added = models.DateTimeField(auto_now_add=True) 


    def __str__(self):
        return self.email 

class NewsLetter(models.Model): #esto es el modelo es decir lo que le llegara al usuario 
    name = models.CharField 
