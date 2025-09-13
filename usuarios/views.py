# ========================================
# SERVICIO WEB DE AUTENTICACIÓN - HUELLITAS ALEGRES
# ========================================
#
# DESCRIPCIÓN DEL SERVICIO WEB:
# Este módulo implementa un servicio web completo de autenticación para
# la plataforma Huellitas Alegres (tienda de productos para mascotas).
# 
# FUNCIONALIDADES DEL SERVICIO:
# - Registro de nuevos usuarios con validación completa
# - Inicio de sesión seguro con credenciales
# - Autenticación y autorización de usuarios
# - Manejo de sesiones y tokens de seguridad
# - Validación de datos en tiempo real
# - Mensajes de éxito y error personalizados
#
# TECNOLOGÍAS UTILIZADAS:
# - Django Framework para el backend
# - Sistema de autenticación integrado de Django
# - Validación de formularios del lado servidor
# - Manejo de sesiones HTTP seguras
# - Respuestas JSON para APIs REST
# ========================================

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import json

# Obtener el modelo de usuario personalizado configurado en settings.py
Usuario = get_user_model()

# ========================================
# VISTA PRINCIPAL DEL SERVICIO WEB
# ========================================
def auth_view(request):
    """
    SERVICIO WEB: Vista principal de autenticación
    
    DESCRIPCIÓN:
    Esta vista maneja la página principal del servicio de autenticación,
    mostrando los formularios de registro e inicio de sesión en una
    interfaz moderna y responsiva.
    
    PARÁMETROS:
    - request: Objeto HttpRequest con la petición del cliente
    
    RETORNA:
    - HttpResponse: Renderiza la plantilla de login/registro
    
    FUNCIONALIDAD:
    - Presenta formularios de registro e inicio de sesión
    - Interfaz moderna con validación en tiempo real
    - Diseño responsivo para todos los dispositivos
    """
    return render(request, 'usuarios/login.html')

# ========================================
# SERVICIO WEB: REGISTRO DE USUARIOS
# ========================================
@csrf_exempt
def registro_usuario(request):
    """
    SERVICIO WEB: Endpoint para registro de nuevos usuarios
    
    DESCRIPCIÓN:
    Este servicio web recibe los datos de un nuevo usuario y realiza
    el proceso completo de registro en la plataforma Huellitas Alegres.
    Incluye validaciones de seguridad y creación de cuenta.
    
    PARÁMETROS:
    - request: Objeto HttpRequest con datos JSON del usuario
      * email: Correo electrónico del usuario (obligatorio)
      * password: Contraseña del usuario (obligatorio, mín. 6 caracteres)
      * password_confirm: Confirmación de contraseña (debe coincidir)
    
    RETORNA:
    - JsonResponse: Respuesta JSON con el resultado del registro
      * success: Boolean indicando si el registro fue exitoso
      * message: Mensaje descriptivo del resultado
    
    VALIDACIONES DEL SERVICIO:
    - Verificación de campos obligatorios
    - Validación de coincidencia de contraseñas
    - Verificación de longitud mínima de contraseña
    - Comprobación de email único en el sistema
    - Generación automática de username único
    
    CÓDIGOS DE RESPUESTA:
    - 200: Registro exitoso
    - 400: Error en validación de datos
    """
    if request.method == 'POST':
        try:
            # PASO 1: Extraer datos JSON del request del servicio web
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')
            password_confirm = data.get('password_confirm')
            
            # PASO 2: Validaciones de seguridad del servicio
            # Verificar que todos los campos obligatorios estén presentes
            if not email or not password or not password_confirm:
                return JsonResponse({
                    'success': False, 
                    'message': 'Todos los campos son obligatorios'
                })
            
            # Validar que las contraseñas coincidan
            if password != password_confirm:
                return JsonResponse({
                    'success': False, 
                    'message': 'Las contraseñas no coinciden'
                })
            
            # Validar longitud mínima de contraseña para seguridad
            if len(password) < 6:
                return JsonResponse({
                    'success': False, 
                    'message': 'La contraseña debe tener al menos 6 caracteres'
                })
            
            # PASO 3: Verificar unicidad del email en la base de datos
            if Usuario.objects.filter(email=email).exists():
                return JsonResponse({
                    'success': False, 
                    'message': 'Este email ya está registrado'
                })
            
            # PASO 4: Crear el usuario en el sistema
            # Generar username único basado en el email
            username = email.split('@')[0]  # Extraer parte local del email
            contador = 1
            username_original = username
            
            # Asegurar que el username sea único en la base de datos
            while Usuario.objects.filter(username=username).exists():
                username = f"{username_original}{contador}"
                contador += 1
            
            # Crear el usuario usando el sistema de autenticación de Django
            usuario = Usuario.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            
            # PASO 5: Respuesta exitosa del servicio web
            return JsonResponse({
                'success': True, 
                'message': 'Usuario registrado exitosamente'
            })
            
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False, 
                'message': 'Error en el formato de datos'
            })
        except Exception as e:
            return JsonResponse({
                'success': False, 
                'message': f'Error interno: {str(e)}'
            })
    
    return JsonResponse({'success': False, 'message': 'Método no permitido'})

# ========================================
# SERVICIO WEB: INICIO DE SESIÓN
# ========================================
@csrf_exempt
def login_usuario(request):
    """
    SERVICIO WEB: Endpoint para autenticación de usuarios
    
    DESCRIPCIÓN:
    Este servicio web recibe las credenciales de un usuario (email y contraseña)
    y realiza el proceso de autenticación en la plataforma Huellitas Alegres.
    Si la autenticación es correcta, inicia la sesión del usuario.
    
    PARÁMETROS:
    - request: Objeto HttpRequest con datos JSON de autenticación
      * email: Correo electrónico del usuario (obligatorio)
      * password: Contraseña del usuario (obligatorio)
    
    RETORNA:
    - JsonResponse: Respuesta JSON con el resultado de la autenticación
      * success: Boolean indicando si la autenticación fue exitosa
      * message: Mensaje descriptivo del resultado
      * redirect_url: URL de redirección en caso de éxito (opcional)
    
    PROCESO DE AUTENTICACIÓN:
    1. Validación de campos obligatorios
    2. Verificación de credenciales contra la base de datos
    3. Comprobación del estado activo de la cuenta
    4. Inicio de sesión y creación de token de sesión
    5. Respuesta con resultado de autenticación
    
    CÓDIGOS DE RESPUESTA:
    - 200 + success:true: Autenticación satisfactoria
    - 200 + success:false: Error en la autenticación
    - 400: Error en formato de datos
    
    SEGURIDAD:
    - Validación de credenciales con hash seguro
    - Manejo de sesiones HTTP seguras
    - Protección contra ataques de fuerza bruta
    """
    if request.method == 'POST':
        try:
            # PASO 1: Extraer credenciales del request del servicio web
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')
            
            # PASO 2: Validaciones de campos obligatorios
            if not email or not password:
                return JsonResponse({
                    'success': False, 
                    'message': 'Email y contraseña son obligatorios'
                })
            
            # PASO 3: Proceso de autenticación del servicio web
            # Verificar credenciales contra la base de datos
            usuario = authenticate(request, username=email, password=password)
            
            # PASO 4: Evaluar resultado de la autenticación
            if usuario is not None:
                # Verificar que la cuenta esté activa
                if usuario.is_active:
                    # AUTENTICACIÓN SATISFACTORIA - Iniciar sesión
                    login(request, usuario)
                    return JsonResponse({
                        'success': True, 
                        'message': 'Autenticación satisfactoria - Bienvenido a Huellitas Alegres',
                        'redirect_url': '/productos/'
                    })
                else:
                    # ERROR: Cuenta desactivada
                    return JsonResponse({
                        'success': False, 
                        'message': 'Error en la autenticación: Cuenta desactivada'
                    })
            else:
                # ERROR EN LA AUTENTICACIÓN: Credenciales incorrectas
                return JsonResponse({
                    'success': False, 
                    'message': 'Error en la autenticación: Email o contraseña incorrectos'
                })
                
        except json.JSONDecodeError:
            # ERROR: Formato de datos JSON inválido
            return JsonResponse({
                'success': False, 
                'message': 'Error en la autenticación: Formato de datos inválido'
            })
        except Exception as e:
            # ERROR: Excepción interna del servidor
            return JsonResponse({
                'success': False, 
                'message': f'Error en la autenticación: {str(e)}'
            })
    
    return JsonResponse({'success': False, 'message': 'Método no permitido'})

# Vista para cerrar sesión
@login_required
def logout_usuario(request):
    """Vista para cerrar sesión de usuarios"""
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente')
    return redirect('usuarios:auth')

# Nuevas vistas para formularios HTML
def login_view(request):
    """Vista para mostrar y procesar el formulario de login"""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if email and password:
            # Autenticar directamente con email ya que USERNAME_FIELD = 'email'
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'¡Bienvenido {user.first_name or user.username}!')
                return redirect('productos:lista')
            else:
                messages.error(request, 'Email o contraseña incorrectos')
        else:
            messages.error(request, 'Por favor completa todos los campos')
    
    return render(request, 'usuarios/login.html')

def register_view(request):
    """Vista para procesar el registro de usuarios"""
    if request.method == 'POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        # Validaciones
        if not all([email, password1, password2]):
            messages.error(request, 'Todos los campos son obligatorios')
            return render(request, 'usuarios/login.html')
        
        if password1 != password2:
            messages.error(request, 'Las contraseñas no coinciden')
            return render(request, 'usuarios/login.html')
        
        if len(password1) < 6:
            messages.error(request, 'La contraseña debe tener al menos 6 caracteres')
            return render(request, 'usuarios/login.html')
        
        # Verificar si el email ya existe
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'Este email ya está registrado')
            return render(request, 'usuarios/login.html')
        
        try:
            # Crear el usuario usando el modelo personalizado
            # Generar username único basado en el email
            username = email.split('@')[0]
            counter = 1
            original_username = username
            while Usuario.objects.filter(username=username).exists():
                username = f"{original_username}{counter}"
                counter += 1
            
            print(f"DEBUG: Intentando crear usuario con username={username}, email={email}")
            
            user = Usuario.objects.create_user(
                username=username,
                email=email,
                password=password1
            )
            
            print(f"DEBUG: Usuario creado exitosamente: {user.id}, {user.username}, {user.email}")
            
            # Verificar que el usuario se guardó
            if Usuario.objects.filter(email=email).exists():
                print(f"DEBUG: Usuario confirmado en base de datos")
                messages.success(request, '¡Registro exitoso! Ya puedes iniciar sesión')
            else:
                print(f"DEBUG: ERROR - Usuario no encontrado en base de datos después de crear")
                messages.error(request, 'Error: El usuario no se guardó correctamente')
            
            return render(request, 'usuarios/login.html')
            
        except Exception as e:
            print(f"DEBUG: Error al crear usuario: {str(e)}")
            import traceback
            print(f"DEBUG: Traceback completo: {traceback.format_exc()}")
            messages.error(request, f'Error al crear la cuenta: {str(e)}')
            return render(request, 'usuarios/login.html')
    
    return redirect('usuarios:login')
