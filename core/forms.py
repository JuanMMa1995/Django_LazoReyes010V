from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Producto, Marca

class ProductoForm(forms.ModelForm):

    class Meta: 
        model= Producto
        fields = ['nombre', 'precio', 'marca', 'fec_fabricacion', 'imagen']
        labels ={
            'nombre': 'Nombre', 
            'precio': 'Precio', 
            'marca': 'Marca', 
            'fec_fabricacion': 'Fec_fabricacion',
            'imagen' :'Imagen',
        }
        widgets={
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ), 
            'precio': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese precio', 
                    'id': 'precio'
                }
            ), 
            'marca': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'marca',
                }
            ),
            'fec_fabricacion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese fec_fabricacion', 
                    'id': 'fec_fabricacion'
                }
            ), 
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese imagen', 
                    'id': 'imagen'
                }
            ), 
            

        }
