from django.db import models
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager, models.Manager):
    
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username=username,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields            
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    # los False hacen referencia los is_staff, is_superuser que son atributos boolianos puede o no puede
    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)
    
    
    # los True hacen referencia los is_staff, is_superuser que son atributos boolianos puede o no puede
    def create_superuser(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, True, True, **extra_fields)