# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView
from wagtail.wagtailcore.models import Page, Site
from users.models import User

class LoginView(TemplateView):
    template_name = "users/login_signup.html"

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['page'] = Site.objects.get(pk=self.request.site.pk).root_page
        context['is_login'] = True
        return context
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')    
            else:
                msg = 'Usuario o contraseña incorrectas'           
        except Exception as e:
            msg = str(e)

        messages.add_message(request, messages.WARNING, msg)

        return redirect('login')

        return super(LoginView, self).render_to_response(context)

class SignupView(TemplateView):
    template_name = "users/login_signup.html"

    def get_context_data(self, **kwargs):
        context = super(SignupView, self).get_context_data(**kwargs)
        context['page'] = Site.objects.get(pk=self.request.site.pk).root_page
        context['is_login'] = False
        return context
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        redirect_url = 'signup'
        try:
            email = request.POST['email']
            password = request.POST['password']
            password = make_password(password)
            user = User(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                telephone_number = request.POST['telephone_number'],
                id_type = request.POST['id_type'],
                id_number = request.POST['id_number'],
                email = email,
                username = email,
                password = password
            )
            user.save()
        except KeyError:
            msg = 'Datos incompletos'
            tag = messages.WARNING
        except IntegrityError:
            msg = 'Ya existe un usuario con el correo o númerio de identificación registrado'
            tag = messages.WARNING
        except Exception as e:
            msg = 'Error al intentar registrarte: ' + str(e)
            tag = messages.WARNING
        else:
            msg = 'Registro exitoso, revisa tu correo electrónico para completar el proceso'
            tag = messages.SUCCESS
            redirect_url = 'login'

        messages.add_message(request, tag, msg)
        
        return redirect(redirect_url)

        return super(SignupView, self).render_to_response(context)

def logout_user(request):
    logout(request)
    messages.add_message(request, messages.INFO, 'Sesión cerrada correctamente')
    return redirect('/')

            
