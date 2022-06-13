from django.contrib import admin
from django.urls import path
from .views import index, galeriaDeAdopcion, api, quienesSomos, productos, registroUsuario, form_crear_Producto, from_modificar_producto
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name="index"),
    path('galeriaDeAdopcion/', galeriaDeAdopcion, name="galeriaDeAdopcion"),
    path('api/', api, name="api"),
    path('quienesSomos/', quienesSomos, name="quienesSomos"),
    path('productos/', productos, name="productos"),
    path('registroUsuario/', registroUsuario, name="registroUsuario"),
    path('form_crear_Producto/', form_crear_Producto, name="form_crear_Producto"),
    path('from_modificar_producto/', from_modificar_producto, name="from_modificar_producto"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)