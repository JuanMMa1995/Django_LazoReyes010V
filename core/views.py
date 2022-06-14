from django.shortcuts import render, redirect
from .models import Producto, contacto
from .forms import ProductoForm, contactoForm

#Create yout views here.
def index(request):
    return render(request, 'index.html')

def galeriaDeAdopcion(request):
    return render(request, 'galeriaDeAdopcion.html')

def quienesSomos(request):
    return render(request, 'quienesSomos.html')

def registroUsuario(request):
    return render(request, 'registroUsuario.html')

def api(request):
    return render(request, 'api.html')

def productos(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'productos.html', data)

def contactoForm(request):
    data ={
        'form':contacto()
    }

    if request.method== 'POST':
        formulario = contactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guargado"
        else:
            data["form"] = formulario

    return render (request, 'contacto.html', data)



def form_crear_Producto(request):
    if request.method=='POST':
        producto_form == ProductoForm (request.POST)
        if producto_form.is_valid():
            producto_form.save()
            return redirect (to="productos")
    else:
        producto_form=ProductoForm()
    return render (request, 'form_crear_producto.html',{'producto_form': producto_form})

def from_modificar_producto(request, id):
    producto =Producto.objects.get(nombre=id)
    datos = {
        'form': ProductoForm(instance = producto)
    }
    if request.method=='POST':
        formulario = ProductoForm(data=request.POST, instance = producto)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="productos")
        data ['form']=formulario
    return render(request, 'from_modificar_producto.html', datos)



