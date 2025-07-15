from django.shortcuts import render, redirect # Importa funciones para renderizar plantillas y redireccionar
from .models import registro # Importa el modelo Registro
from django.contrib.auth import authenticate, login, logout # Importa funciones de autenticación
from django.contrib.auth.decorators import login_required # Importa el decorador para requerir login
# Importa el módulo 'viewsets' de Django REST Framework, que permite crear vistas basadas en conjuntos
# de modelos (ModelViewSet, ReadOnlyModelViewSet, etc.).
from rest_framework import viewsets
# Importa la clase 'IsAuthenticated', que es una restricción de permisos para que solo usuarios autenticados
# puedan acceder a ciertas vistas.
from rest_framework.permissions import IsAuthenticated
# Importa el serializador 'RegistroSerializer' desde el archivo serializers.py del mismo directorio.
# Los serializadores se usan para convertir instancias de modelos a formatos como JSON y viceversa.
from .serializers import registroSerializer

# Importa el conjunto de vistas genéricas para modelos de Django REST Framework
class RegistroViewSet(viewsets.ModelViewSet):
    # Define el conjunto de datos (queryset) que este ViewSet manejará, en este caso, todos los objetos Registro
    queryset = registro.objects.all()
    # Especifica el serializador que se usará para convertir instancias de Registro a JSON y viceversa
    serializer_class = registroSerializer
    # Define las clases de permisos; aquí, solo usuarios autenticados pueden acceder a este ViewSet
    permission_classes = [IsAuthenticated]