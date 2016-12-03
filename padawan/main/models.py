# -*- coding: utf-8 -*-
from django.db import models
from wagtail.wagtailadmin.edit_handlers import (TabbedInterface, ObjectList,
                                                InlinePanel, FieldPanel)
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailcore.models import Page, Orderable
from modelcluster.fields import ParentalKey
from products.models import Product, Category
from wagtail.contrib.settings.models import BaseSetting, register_setting

@register_setting
class SocialMediaSettings(BaseSetting):
    facebook = models.URLField(help_text='URl a tu página de Facebook')
    instagram = models.CharField(max_length=255, help_text='Tu usuario de Instagram, sin el @')
    twitter = models.CharField(max_length=255, help_text='Tu usuario de Twitter, sin el @')
    youtube = models.URLField(help_text='URL a tu canal de Youtube')

    class Meta:
        verbose_name = 'Cuenta de red social'
        verbose_name = 'Cuentas de redes sociales'

@register_setting
class PayUSettings(BaseSetting):
    merchant_id = models.CharField(max_length=255, help_text='Tu id de comercio de PayU')
    account_id = models.CharField(max_length=255, help_text='Tu id de cuenta de PayU')
    api_login = models.CharField(max_length=255, help_text='API login de integración')
    api_key = models.CharField(max_length=255, help_text='API Key de integración')

    class Meta:
        verbose_name = 'Configuracion PayU'
        verbose_name = 'Configuraciones PayU'

class Picture(models.Model):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    panels = [
        ImageChooserPanel('image'),
    ]

class MerchantPagePicture(Orderable, Picture):
    page = ParentalKey('main.MerchantPage', related_name='pictures')

class MerchantPage(Page):
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    def get_context(self, request):
        context = super(MerchantPage, self).get_context(request)
        context['product_list'] = Product.objects.order_by('?')[:8]
        context['random_categories'] = Category.objects.order_by('?')[:2]
        return context

    subpage_types = ['products.Category']

    content_panels = [
        ImageChooserPanel('logo')
    ]
    main_slide_panels = [
        InlinePanel('pictures', label='Slide principal')
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Configuración general'),
        ObjectList(main_slide_panels, heading='Slide principal'),
        ObjectList(Page.promote_panels, heading='SEO')
    ])