from django.db import models  # Importa el módulo de modelos de Django

# Modelo Producto
class registro(models.Model):  # Define una clase llamada Producto que hereda de models.Model
    coderg = models.IntegerField()  # Campo de texto para el nombre del producto, máximo 100 caracteres
    codusuario = models.IntegerField()  # Campo de texto largo para la descripción del producto
    codlibro = models.IntegerField()  # Campo decimal para el precio, hasta 10 dígitos y 2 decimales
    sexo = models.TextField()  
    autor = models.TextField()  
    Fsalida = models.TextField() 
    Fentrega = models.TextField() 
    def __str__(self):  # Método especial para representar el objeto como una cadena
        return self.registro  # Devuelve el nombre del producto como representación en texto
