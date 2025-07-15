# Importa el router por defecto de DRF, que ayuda a generar URLs automáticamente para viewsets.
from rest_framework.routers import DefaultRouter

# Importa el viewset 'ProductoViewSet' desde el archivo views.py del mismo módulo.
from .views import RegistroViewSet, RegistroViewSet

# Crea una instancia del DefaultRouter, que gestionará las rutas de la API.
router = DefaultRouter()

# Registra el viewset 'ProductoViewSet' bajo el prefijo 'registro'.
# Esto significa que las URLs generadas serán del tipo /registro/, /registro/{id}/, etc.
# El 'basename' se usa para nombrar las rutas y evitar conflictos si hay varios viewsets similares.
router.register(r'registro', RegistroViewSet, basename='registro')

# Asigna a 'urlpatterns' todas las URLs generadas automáticamente por el router.
urlpatterns = router.urls

# Esto permite que Django reconozca y enrute las peticiones HTTP a los métodos
# correspondientes del viewset.