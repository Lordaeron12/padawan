# -*- coding: utf-8 -*-
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import Feature


class FeatureModelAdmin(ModelAdmin):
    model = Feature
    menu_label = 'Características'  
    menu_icon = 'snippet'  
    menu_order = 200 
    add_to_settings_menu = False  #
    list_display = ('name',)
    search_fields = ('name',)

modeladmin_register(FeatureModelAdmin)