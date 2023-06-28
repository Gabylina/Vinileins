"""
URL configuration for servidor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from aplicaciones import views

#URLS.py Servidorcito
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aplicaciones.urls')),
    path('detalle/<int:id>/', views.detalle, name='detalle'),
    path('accounts/', include('django.contrib.auth.urls')),

    # path('vin_pop/<int:estilo>/', views.vin_pop, name='vin_pop'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)