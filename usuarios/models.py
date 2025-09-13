from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Modelo personalizado de Usuario que extiende AbstractUser
class Usuario(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Correo Electrónico')
    fecha_registro = models.DateTimeField(default=timezone.now, verbose_name='Fecha de Registro')
    is_active = models.BooleanField(default=True, verbose_name='Activo')
    
    # Usar email como campo de autenticación en lugar de username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'usuarios_usuario'
    
    def __str__(self):
        return f'{self.email} - {self.username}'
