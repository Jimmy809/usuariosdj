from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.

# con esta class vamos a reutilizar la base de django sobre user, agregandole mas parametros y permisos a los user
class User(AbstractBaseUser, PermissionsMixin):
    # aqui declaramos la seleccion que va a tener la variable genero, por el choices agregado
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros'),

    )
    # aqui creamos los campos de la base de datos
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    genero = models.CharField(max_length=1, choices = GENDER_CHOICES, blank=True)
    
    # necesitamos decirle a django con que se hara el login
    USERNAME_FIELD = 'username'

    # funcion para nombre corto
    def get_short_name(self):
        return self.username
    
    # funcion para nombre largo, concatenemos nombres y apellidos
    def get_full_name(self):
        return self.nombres + ' ' + self.apellidos