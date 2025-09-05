from django.db import models # Importamos el módulo models de Django


class Producto(models.Model): # Modelo para representar un producto
   # Definimos los campos del modelo
   nombre = models.CharField(max_length=100)  # nombre del producto
   descripcion = models.TextField()            # descripción larga
   precio = models.DecimalField(max_digits=10, decimal_places=2)
   cantidad_stock = models.IntegerField()
   fecha_creacion = models.DateField(auto_now_add=True)
   fecha_ultima_modificacion = models.DateField(auto_now=True)


   def __str__(self):
       return self.nombre


   class Meta:
       db_table = 'productos'  # aquí definimos el nombre exacto de la tabla
       
