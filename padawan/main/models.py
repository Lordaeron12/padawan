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
class PayUSettings(BaseSetting):
    merchant_id = models.CharField(max_length=255, help_text='Tu id de comercio de PayU')
    account_id = models.CharField(max_length=255, help_text='Tu id de cuenta de PayU')
    api_login = models.CharField(max_length=255, help_text='API login de integración')
    api_key = models.CharField(max_length=255, help_text='API Key de integración')

    class Meta:
        verbose_name = 'Configuracion PayU'
        verbose_name = 'Configuraciones PayU'

class ContactConfig(models.Model):
    city = models.CharField(
        'Ciudad',
        max_length=50,
        blank=True,
        null=True
    )
    tel_number = models.CharField(
        "Número telefónico",
        max_length=25,
        blank=True,
        null=True
    )
    email = models.EmailField(
        "Correo electrónico",
        blank=True,
        null=True,
        help_text='Si quieres cambiar el correo predeterminado de notificaciones, cambia tu email de cuenta'
    )
    
    panels = [
        FieldPanel('city'),
        FieldPanel('tel_number'),
        FieldPanel('email'),
    ]

class SocialMediaLink(models.Model):
    SOCIAL_NETWORK_CHOICES = (
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('instagram', 'Instagram'),
        ('youtube', 'Youtube'),
        ('snapchat', 'Snapchat'),
        ('pinterest', 'Pinterest'),
        ('googleplus', 'Google +'),
    )
    network = models.CharField(
        max_length=15,
        choices=SOCIAL_NETWORK_CHOICES,
        default="facebook", 
        blank=True,
        null=True
    )
    link = models.URLField(
        "Enlace a la red social",
        blank=True,
        null=True
    )
    
    panels = [
        FieldPanel('network'),
        FieldPanel('link'),
    ]

class Picture(models.Model):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    title = models.CharField(
        'Título',
        max_length = 50,
        null = True,
        blank = True
    )
    description = models.CharField(
        'Descripción',
        max_length = 150,
        null = True,
        blank = True
    )
    link = models.URLField(
        null = True,
        blank = True
    )

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('link'),
    ]

class MerchantPageSlidePicture(Orderable, Picture):
    page = ParentalKey('main.MerchantPage', related_name='related_slide_pictures')

class MerchantPageRelatedSocialMediaLink(Orderable, SocialMediaLink):
    page = ParentalKey('main.MerchantPage', related_name='related_social_media_links')

class MerchantPageRelatedContactConfig(Orderable, ContactConfig):
    page = ParentalKey('main.MerchantPage', related_name='related_contact_config')

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
        FieldPanel('title'),
        ImageChooserPanel('logo')
    ]
    main_slide_panels = [
        InlinePanel('related_slide_pictures', label='Slide principal')
    ]
    social_panels = [
        InlinePanel('related_social_media_links', label='Redes sociales')
    ]
    contact_panels = [
        InlinePanel('related_contact_config', label='Contacto')
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Configuración general'),
        ObjectList(main_slide_panels, heading='Slide principal'),
        ObjectList(social_panels, heading='Redes sociales'),
        ObjectList(contact_panels, heading='Contacto'),
        ObjectList(Page.promote_panels, heading='SEO')
    ])