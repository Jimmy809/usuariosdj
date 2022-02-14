from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

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
    nombres = models.CharField(max_length=30, blank=True)
    apellidos = models.CharField(max_length=30, blank=True)
    genero = models.CharField(max_length=1, choices = GENDER_CHOICES, blank=True)
    codregistro = models.CharField(max_length=6, blank=True)
    # todo aqui q se registr por definicion no sera staff
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    # necesitamos decirle a django con que se hara el login
    USERNAME_FIELD = 'username'
    
    # para que la consola nos pida el email ya que es obligatorio para crear el usuario
    # despues de la , podemos seguir agregando parametros paraq nos lo pida por consola
    REQUIRED_FIELDS = ['email',] 
    
    objects = UserManager()

    # funcion para nombre corto
    def get_short_name(self):
        return self.username
    
    # funcion para nombre largo, concatenemos nombres y apellidos
    def get_full_name(self):
        return self.nombres + ' ' + self.apellidos