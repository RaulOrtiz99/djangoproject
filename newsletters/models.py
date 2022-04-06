import email
from django.db import models

# Create your models here.

#Estos son los modelos del usuario

class NewsLetterUser(models.Model): #este es el modelo para el usuario
    email = models.EmailField(null=False, unique=True)
    date_added = models.DateTimeField(auto_now_add=True) 


    def __str__(self):
        return self.email 

class NewsLetter(models.Model): #este modelo es el email que le llegara al usuario 
    name = models.CharField(max_length=250) #esto es como decir el titulo del correo que haremos
    subject = models.CharField(max_length=250)#esto es el tema de lo que hablamos en el correo
    body = models.TextField(blank=True, null=True)#esto es el contenido del proyecto 
    email = models.ManyToManyField(NewsLetterUser) #relacion entre modelos
    created = models.DateTimeField(auto_now_add=True)#info para saber cuando fue creado el email 

    def __str__(self):
        return self.name

