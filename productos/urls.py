

from django.urls import path
from .views import lista_productos, create_product, edit_product, delete_product

urlpatterns = [
   path('', lista_productos, name='lista'),
   path('nuevo/', create_product, name='nuevo'),
   path('editar/<int:pk>/', edit_product, name='editar'),
   path('eliminar/<int:pk>/', delete_product, name='eliminar'),
]
