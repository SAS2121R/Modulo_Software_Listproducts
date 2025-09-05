from django import forms #importamos el modulo forms de Django
from .models import Producto # Importamos el modelo Producto


class ProductoForm(forms.ModelForm):
   class Meta: 
       model = Producto
       fields = ['nombre', 'descripcion', 'precio', 'cantidad_stock']
       