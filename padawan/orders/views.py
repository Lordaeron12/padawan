from django.core.exceptions import SuspiciousOperation
from django.http import JsonResponse

from products.models import Product, Variant
from .models import Order, OrderItem


def get_product_variants(request):
    if request.is_ajax():
         if 'product_id' in request.GET.keys():
            product = Product.objects.get(pk=request.GET['product_id'])
            response = JsonResponse(
                list(product.get_variants().values('value', 'price', 'pk')),
                safe = False
            )
            return response
    raise SuspiciousOperation("Invalid request")

def get_variant(request):
    if request.is_ajax():
         if 'variant_id' in request.GET.keys():
            variant = Variant.objects.values().get(pk=request.GET['variant_id'])
            response = JsonResponse(
                variant,
                safe = False
            )
            return response
    raise SuspiciousOperation("Invalid request")

def add_to_cart(request):
    if request.is_ajax():
         if 'variant_id' and 'is_temp' and 'quantity' and 'user' or 'cart_id' in request.POST.keys():
            print request.POST
            response = JsonResponse(
                {
                    'response': 'valid'
                }
            )
            return response
    raise SuspiciousOperation("Invalid request")