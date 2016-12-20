from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    city = models.ForeignKey('orders.City', null=True, blank=True)

    def __str__(self):
        return self.username
