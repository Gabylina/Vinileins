from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, otrawea, vinilos, añadir, modificarvinilo, iniciocliente, detalle, viniloscli, listar_vinilos,\
    listar_vinilos_vini, pagar_log_required , registro

#URLS.py aplicaciones
urlpatterns = [
    path('',index,name='index'), # index para ver los vinilos y gestionarlos
    path('otrawea',otrawea,name='otrawea'),
    path('vinilos',vinilos,name='vinilos'),
    path('añadir',añadir,name='añadir'),
    path('modificarvinilo/<id>',modificarvinilo,name="modificarvinilo"),
    path('iniciocliente',listar_vinilos,name='iniciocliente'),
    path('detalle',detalle, name='detalle'),
    path('viniloscli',listar_vinilos_vini, name='viniloscli'),
    path('pagar_log_required',pagar_log_required,name="pagar_log_required"),
    path('registro',registro,name='registro'),
    
    # path('vin_pop',vin_pop, name='vin_pop'),
    
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)