from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

# Configuración personalizada del admin para Usuario
class UsuarioAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_active', 'fecha_registro')
    list_filter = ('is_active', 'is_staff', 'fecha_registro')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('-fecha_registro',)
    
    # Campos que se muestran en el formulario de edición
    fieldsets = UserAdmin.fieldsets + (
        ('Información Adicional', {'fields': ('fecha_registro',)}),
    )
    
    # Campos de solo lectura
    readonly_fields = ('fecha_registro',)

# Registrar el modelo Usuario con la configuración personalizada
admin.site.register(Usuario, UsuarioAdmin)
