from django.db import models
from products.models import Variant
from users.models import User

class State(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class City(models.Model): 
    name = models.CharField(max_length=50)
    state = models.ForeignKey(State)

    def __str__(self):
        return self.name

class Order(models.Model):
    ORDER_STATUS_CHOICES = (
        ('IP', 'En progreso'),
        ('PE', 'Pendiente'),
        ('CO', 'Confirmada'),
        ('DL', 'Enviada'),
        ('CA', 'Cancelada'),
    )
    customer = models.ForeignKey(User, null=True, blank=True)
    session_id = models.CharField(max_length=255, null=True)
    shipping_address = models.CharField(max_length=255, null=True, blank=True)
    shipping_city = models.ForeignKey(City, null=True, blank=True)
    status = models.CharField(max_length=2, choices=ORDER_STATUS_CHOICES, default="IP")

    def __str__(self):
        return 'Compra ' + self.pk

class OrderItem(models.Model):
    order = models.ForeignKey(Order)
    reference = models.ForeignKey(Variant)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.pk

class Shipping(models.Model):
    order = models.ForeignKey(Order)
    shipping_code = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.shipping_code