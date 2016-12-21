# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ID_CHOICES = (
        ('CC', 'Cédula de ciudadanía'),
        ('TI', 'Tarjeta de identidad'),
        ('CE', 'Cédula de extranjería'),
        ('NIT', 'NIT'),
        ('PA', 'Pasaporte'),
    )
    telephone_number = models.CharField(max_length=25, null=True, blank=True)
    id_type = models.CharField(max_length=3, null=True, blank=True, choices=ID_CHOICES)
    id_number = models.CharField(max_length=15, null=True, blank=True, unique=True)

    def __str__(self):
        return self.username
