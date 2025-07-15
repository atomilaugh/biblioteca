from django.contrib import admin
from django.urls import path
from registro import views

# Importa el módulo de administración de Django, que permite gestionar el sitio de administración.
from django.contrib import admin

# Importa las funciones 'path' e 'include' para definir rutas y agregar otras configuraciones de URLs.
from django.urls import path, include

# Importa las vistas del módulo 'registor', aunque en este archivo no se usan directamente.
from registro import views

# Lista donde se definen todas las rutas de la aplicación.
urlpatterns = [
    # Incluye las URLs definidas en el archivo 'api_urls' dentro de la app 'registor'.
    # Todas las rutas incluidas aquí estarán bajo el prefijo 'api/'.
    path('api/', include('registro.api_urls')),

    # Incluye las URLs de autenticación proporcionadas por Django REST Framework.
    # Esto permite el inicio de sesión tradicional en el navegador para la API.
    path('api-auth/', include('rest_framework.urls')), # Login tradicional en navegador
]