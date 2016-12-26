# -*- coding: utf-8 -*-
from django.contrib import messages
from django.core.exceptions import SuspiciousOperation, ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt

from products.models import Product, Variant
from users.models import User
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

def get_card_id(request):
    if request.is_ajax():
         if 'user_id' in request.GET.keys():
            try:
                order_id = Order.objects.get(customer__pk=request.GET['user_id'], status='IP').values('pk')
            except (ObjectDoesNotExist, ValueError):
                order_id = {
                    'pk': None    
                }
            response = JsonResponse(
                order_id,
                safe = False
            )
            return response
    raise SuspiciousOperation("Invalid request")

def add_to_cart(request):
    if request.method == "POST":
        referer = request.META['HTTP_REFERER']
        try:
            reference_id = request.POST['reference_id']
            quantity = request.POST['quantity']
        except KeyError:
            messages.add_message(
                request,
                messages.WARNING,
                'Petición inválida'
            )
            return redirect(referer)
        else:
            if not request.user.is_authenticated():
                messages.add_message(
                    request,
                    messages.WARNING,
                    'Inicia sesión para disfrutar de nuestros productos'
                )
                return redirect('login')

            user = request.user

            try:
                in_progress_cart = Order.objects.get(customer=user, status="IP")
            except ObjectDoesNotExist:
                in_progress_cart = None
            
            if not in_progress_cart:
                order = Order(
                    customer = user
                )
                order.save()

            if reference_id and quantity:
                reference = Variant.objects.get(pk=reference_id)
                order_item = OrderItem(
                    reference = reference,
                    order = in_progress_cart,
                    quantity = quantity
                )
                order_item.save()
                msg = 'Producto agregado correctamente'
                tag = messages.SUCCESS
            else:
                msg = 'Olvidaste elegir algunos datos, vuelva a intentarlo'
                tag = messages.WARNING

            messages.add_message(
                request,
                tag,
                msg
            )
            return redirect(referer)
    raise SuspiciousOperation("Invalid request")