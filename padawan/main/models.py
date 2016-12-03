# -*- coding: utf-8 -*-
from django.db import models
from wagtail.wagtailadmin.edit_handlers import (TabbedInterface, ObjectList,
                                                InlinePanel, FieldPanel)
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailcore.models import Page, Orderable
from modelcluster.fields import ParentalKey
from products.models import Product

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