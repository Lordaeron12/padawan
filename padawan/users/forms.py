# -*- coding: utf-8 -*-
from django import forms
from wagtail.wagtailusers.forms import UserEditForm, UserCreationForm
from users.models import User

class CustomUserEditForm(UserEditForm):
    telephone_number = forms.CharField(required=True, label='Número de teléfono')
    id_type = forms.ChoiceField(required=True, label='Tipo de documento', choices=User.ID_CHOICES)
    id_number = forms.CharField(required=True, label='Número de documento')


class CustomUserCreationForm(UserCreationForm):
    telephone_number = forms.CharField(required=True, label='Número de teléfono')
    id_type = forms.ChoiceField(required=True, label='Tipo de documento', choices=User.ID_CHOICES)
    id_number = forms.CharField(required=True, label='Número de documento')