from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Producto, Marca, contacto

class contactoForm(forms.ModelForm):
    class Meta:
        model= contacto
        fields='__all__'

class ProductoForm(forms.ModelForm):

    class Meta: 
        model= Producto
        fields = '__all__'
        labels = '__all__'