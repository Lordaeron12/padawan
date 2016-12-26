from django.conf.urls import include, url
from orders.views import (
    get_product_variants,
    get_variant,
    get_card_id,
    add_to_cart
)

urlpatterns = [
    url(r'^get_product_variants/', get_product_variants, name="get_product_variants"),
    url(r'^get_variant/', get_variant, name="get_variant"),
    url(r'^add_to_cart/', add_to_cart, name="add_to_cart"),
    url(r'^get_card_id/', get_card_id, name="get_card_id"),
]

