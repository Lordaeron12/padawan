from django.db import models
from products.models import Variant

class Order(models.Model):
    ORDER_STATUS_CHOICES = (
        ('IP', 'En progreso'),
        ('PE', 'Pendiente'),
        ('CO', 'Confirmada'),
        ('DL', 'Enviada'),
        ('CA', 'Cancelada'),
    )

    buyer_id = models.CharField(max_length=25)
    buyer_name = models.CharField(max_length=150)
    buyer_phone = models.CharField(max_length=12)
    buyer_address = models.CharField(max_length=255)
    buyer_email = models.CharField(max_length=255)
    buyer_city = models.CharField(max_length=25)
    status = models.CharField(max_length=2, choices=ORDER_STATUS_CHOICES)

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