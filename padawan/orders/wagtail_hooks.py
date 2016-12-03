# -*- coding: utf-8 -*-
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import Order, Shipping


class OrderModelAdmin(ModelAdmin):
    model = Order
    menu_label = 'Compras'  
    menu_icon = 'snippet'  
    menu_order = 200 
    add_to_settings_menu = False  #
    list_display = ('__str__', 'buyer_id', 'buyer_name', 'buyer_phone', 'buyer_email', 'buyer_city', 'status')
    search_fields = ('__str__','buyer_id', 'buyer_name',)

modeladmin_register(OrderModelAdmin)

class ShippingModelAdmin(ModelAdmin):
    model = Shipping
    menu_label = 'Envíos'  
    menu_icon = 'snippet'  
    menu_order = 200 
    add_to_settings_menu = False  #
    list_display = ('__str__','order____str__',)
    search_fields = ('__str__',)

modeladmin_register(ShippingModelAdmin)