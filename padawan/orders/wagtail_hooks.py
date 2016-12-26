# -*- coding: utf-8 -*-
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import Order, Shipping


class OrderModelAdmin(ModelAdmin):
    model = Order
    menu_label = 'Compras'  
    menu_icon = 'plus'  
    menu_order = 200 
    add_to_settings_menu = False  #
    list_display = ('__str__', 'customer', 'status')
    search_fields = ('__str__','customer__id_number', 'customer__first_name', 'customer__last_name')

modeladmin_register(OrderModelAdmin)

class ShippingModelAdmin(ModelAdmin):
    model = Shipping
    menu_label = 'Envíos'  
    menu_icon = 'site'  
    menu_order = 200 
    add_to_settings_menu = False  #
    list_display = ('__str__','order____str__',)
    search_fields = ('__str__',)

modeladmin_register(ShippingModelAdmin)