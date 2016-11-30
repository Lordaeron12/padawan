# -*- coding: utf-8 -*-
from django.db import models
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailadmin.edit_handlers import (TabbedInterface, ObjectList,
                                                PageChooserPanel, FieldPanel,
                                                InlinePanel, MultiFieldPanel)
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Orderable
from modelcluster.fields import ParentalKey
from wagtail.wagtailsearch import index

class Category(Page):
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    intro = models.CharField(max_length=250)

    content_panels = Page.content_panels + [
        ImageChooserPanel('main_image'),
        FieldPanel('intro'),
    ]

class Feature(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Picture(models.Model):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    caption = models.CharField(max_length=255, blank=True)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]

    class Meta:
        abstract = True


class ProductPicture(Orderable, Picture):
    page = ParentalKey('products.Product', related_name='pictures')


class Variant(models.Model):
    feature = models.ForeignKey(Feature, null=True, blank=True)
    value = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product = ParentalKey('products.Product', related_name='variants')
    stock_quantity = models.IntegerField('In stock')

    def __str__(self):
        return self.name

    def get_stock(self):
        return self.stock


class Product(Page):
    description = RichTextField()

    @property
    def name(self):
        return self.title

    def __str__(self):
        return self.name

    content_panels = [
        FieldPanel('title'),
        FieldPanel('description'),
        InlinePanel('pictures', label='Pictures')
    ]
    variant_panels = [
        InlinePanel('variants', label='Variants')
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Product'),
        ObjectList(Page.promote_panels, heading='Promote'),
        ObjectList(variant_panels, heading='Variants')
    ])