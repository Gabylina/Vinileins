from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .views import agregar_Vinilo, buscarapi, carrito, precompra, comprarahora, crearcuenta, eliminar_Vinilo, index, iniciosesion, limpiar_Carrito, modificarestado, otrawea, pedidos, restar_Vinilo, vinilos, añadir, modificarvinilo,añadiradmin,cliente,iniciocliente,eliminarvinilo, detalle, viniloscli, listar_vinilos, listar_vinilos_vini, pago

#URLS.py aplicaciones
urlpatterns = [
    path('',index,name='index'),
    path('otrawea',otrawea,name='otrawea'),
    path('vinilos',vinilos,name='vinilos'),
    path('añadir',añadir,name='añadir'),
    path('modificarvinilo/<id>/',modificarvinilo,name="modificarvinilo"),
    path('eliminarvinilo/<id>/',eliminarvinilo,name="eliminarvinilo"),
    path('añadiradmin',añadiradmin,name='añadiradmin'),
    path('cliente',cliente,name='cliente'),
    path('pedidos',pedidos,name='pedidos'),
    path('modificarestado/<id>/',modificarestado,name='modificarestado'),
    path('iniciocliente',listar_vinilos,name='iniciocliente'),
    path('detalle',detalle, name='detalle'),
    path('viniloscli',listar_vinilos_vini, name='viniloscli'),
    path('carrito',carrito, name='carrito'),
    path('agregar/<int:Vinilo_id>/', agregar_Vinilo, name='add'),
    path('comprarahora/<int:Vinilo_id>/', comprarahora, name='com'),
    path('eliminar/<int:Vinilo_id>/', eliminar_Vinilo, name='del'),
    path('restar/<int:Vinilo_id>/', restar_Vinilo, name='res'),
    path('limpiar', limpiar_Carrito, name='lim'),
    path('pago',pago,name="pago"),
    path('iniciosesion',iniciosesion,name="iniciosesion"),
    path('crearcuenta',crearcuenta,name="crearcuenta"),
    path('buscarapi',buscarapi,name="buscarapi"),
    path('precompra',precompra,name="precompra"),
    # path('vin_pop',vin_pop, name='vin_pop'),
    
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)