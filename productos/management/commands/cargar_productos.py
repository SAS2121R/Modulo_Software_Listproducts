from django.core.management.base import BaseCommand
from productos.models import Producto
from decimal import Decimal
from datetime import date

class Command(BaseCommand):
    """
    Comando personalizado para cargar 30 productos de mascotas en la base de datos
    Uso: python manage.py cargar_productos
    """
    help = 'Carga 30 productos de mascotas en la base de datos'

    def handle(self, *args, **options):
        # Lista de productos a insertar
        productos_data = [
            {
                'nombre': 'Concentrado premium para perros',
                'descripcion': 'Alimento seco de alta calidad para perros adultos de todas las razas, con vitaminas y minerales esenciales.',
                'precio': Decimal('75000.00'),
                'cantidad_stock': 150
            },
            {
                'nombre': 'Juguete interactivo para gatos',
                'descripcion': 'Ratón de felpa con catnip para estimular el instinto de caza y juego en gatos.',
                'precio': Decimal('15500.00'),
                'cantidad_stock': 200
            },
            {
                'nombre': 'Jeringa de 35 ml',
                'descripcion': 'Jeringa desechable de 35 ml con aguja, para administración de medicamentos o fluidos.',
                'precio': Decimal('4500.00'),
                'cantidad_stock': 300
            },
            {
                'nombre': 'Shampoo antipulgas para perros',
                'descripcion': 'Shampoo medicinal con efecto rápido contra pulgas y garrapatas, deja el pelaje suave y brillante.',
                'precio': Decimal('32000.00'),
                'cantidad_stock': 80
            },
            {
                'nombre': 'Collar isabelino talla M',
                'descripcion': 'Collar de protección para evitar que el animal se lama o muerda heridas y vendajes.',
                'precio': Decimal('28000.00'),
                'cantidad_stock': 50
            },
            {
                'nombre': 'Snacks dentales para perros',
                'descripcion': 'Galletas masticables que ayudan a reducir la placa y el sarro, manteniendo los dientes limpios.',
                'precio': Decimal('22500.00'),
                'cantidad_stock': 120
            },
            {
                'nombre': 'Cepillo para pelo de gato',
                'descripcion': 'Cepillo de cerdas suaves para eliminar el exceso de pelo y evitar la formación de bolas de pelo.',
                'precio': Decimal('18000.00'),
                'cantidad_stock': 95
            },
            {
                'nombre': 'Cama ortopédica para perros grandes',
                'descripcion': 'Cama con espuma de memoria para aliviar la presión en las articulaciones de perros mayores o con artritis.',
                'precio': Decimal('120000.00'),
                'cantidad_stock': 25
            },
            {
                'nombre': 'Transportadora para gatos',
                'descripcion': 'Transportadora plástica y ventilada, ideal para viajes cortos o visitas al veterinario.',
                'precio': Decimal('65000.00'),
                'cantidad_stock': 40
            },
            {
                'nombre': 'Suplemento de omega-3',
                'descripcion': 'Gotas de aceite de pescado para mejorar la salud de la piel y el pelaje de perros y gatos.',
                'precio': Decimal('48000.00'),
                'cantidad_stock': 70
            },
            {
                'nombre': 'Antibiótico de amplio espectro',
                'descripcion': 'Medicamento en pastillas para tratar infecciones bacterianas comunes en mascotas.',
                'precio': Decimal('65000.00'),
                'cantidad_stock': 35
            },
            {
                'nombre': 'Guantes de látex desechables',
                'descripcion': 'Caja de 100 guantes para procedimientos veterinarios y manipulación de productos.',
                'precio': Decimal('18500.00'),
                'cantidad_stock': 150
            },
            {
                'nombre': 'Comida húmeda para cachorros',
                'descripcion': 'Paté nutritivo con pollo y arroz para cachorros en crecimiento.',
                'precio': Decimal('12000.00'),
                'cantidad_stock': 180
            },
            {
                'nombre': 'Arenero autolimpiable',
                'descripcion': 'Caja de arena automática para gatos que simplifica la limpieza diaria.',
                'precio': Decimal('250000.00'),
                'cantidad_stock': 15
            },
            {
                'nombre': 'Champú hipoalergénico',
                'descripcion': 'Producto para pieles sensibles, libre de fragancias y colorantes que pueden causar irritación.',
                'precio': Decimal('45000.00'),
                'cantidad_stock': 60
            },
            {
                'nombre': 'Juguete dispensador de comida',
                'descripcion': 'Bola de goma con un orificio para guardar snacks, que fomenta la actividad física y mental.',
                'precio': Decimal('21000.00'),
                'cantidad_stock': 110
            },
            {
                'nombre': 'Gotas para los oídos',
                'descripcion': 'Solución ótica para limpiar y prevenir infecciones en los oídos de perros.',
                'precio': Decimal('38000.00'),
                'cantidad_stock': 45
            },
            {
                'nombre': 'Plato doble de acero inoxidable',
                'descripcion': 'Comedero y bebedero resistente y fácil de limpiar para mascotas.',
                'precio': Decimal('29000.00'),
                'cantidad_stock': 90
            },
            {
                'nombre': 'Bolsas sanitarias para perros',
                'descripcion': 'Rollos de bolsas biodegradables para recoger los desechos de las mascotas.',
                'precio': Decimal('9500.00'),
                'cantidad_stock': 250
            },
            {
                'nombre': 'Venda elástica autoadherente',
                'descripcion': 'Venda flexible para curar lesiones, que no se pega al pelo de los animales.',
                'precio': Decimal('14000.00'),
                'cantidad_stock': 100
            },
            {
                'nombre': 'Spray repelente de insectos',
                'descripcion': 'Producto para rociar en el pelaje que protege contra mosquitos y otros insectos.',
                'precio': Decimal('37500.00'),
                'cantidad_stock': 75
            },
            {
                'nombre': 'Termómetro digital veterinario',
                'descripcion': 'Termómetro de uso rectal con punta flexible para una medición rápida y precisa de la temperatura.',
                'precio': Decimal('55000.00'),
                'cantidad_stock': 30
            },
            {
                'nombre': 'Cortaúñas para mascotas',
                'descripcion': 'Cortaúñas de acero inoxidable con mango antideslizante, ideal para el cuidado de las uñas.',
                'precio': Decimal('26000.00'),
                'cantidad_stock': 85
            },
            {
                'nombre': 'Jaula plegable para perros',
                'descripcion': 'Jaula de metal segura y fácil de armar, perfecta para entrenamientos y viajes.',
                'precio': Decimal('110000.00'),
                'cantidad_stock': 20
            },
            {
                'nombre': 'Pezón de silicona para biberones',
                'descripcion': 'Pezones de repuesto para alimentar cachorros y gatitos huérfanos.',
                'precio': Decimal('8500.00'),
                'cantidad_stock': 150
            },
            {
                'nombre': 'Limpiador de lágrimas para perros',
                'descripcion': 'Solución suave para eliminar manchas de lágrimas alrededor de los ojos de perros de razas pequeñas.',
                'precio': Decimal('19500.00'),
                'cantidad_stock': 65
            },
            {
                'nombre': 'Concentrado para gatos esterilizados',
                'descripcion': 'Alimento especializado para controlar el peso y la salud urinaria en gatos castrados.',
                'precio': Decimal('78000.00'),
                'cantidad_stock': 90
            },
            {
                'nombre': 'Cepillo de dientes de dedo',
                'descripcion': 'Cepillo pequeño y flexible para una limpieza dental suave en perros y gatos.',
                'precio': Decimal('11500.00'),
                'cantidad_stock': 130
            },
            {
                'nombre': 'Correa retráctil para perros',
                'descripcion': 'Correa extensible de 5 metros para paseos seguros y con libertad de movimiento.',
                'precio': Decimal('42000.00'),
                'cantidad_stock': 55
            },
            {
                'nombre': 'Kit de primeros auxilios para mascotas',
                'descripcion': 'Maletín con vendajes, gasas, antiséptico y otros elementos esenciales para emergencias.',
                'precio': Decimal('85000.00'),
                'cantidad_stock': 25
            }
        ]

        # Contador de productos creados
        productos_creados = 0
        productos_existentes = 0

        self.stdout.write(self.style.SUCCESS('Iniciando carga de productos...'))

        for producto_data in productos_data:
            # Verificar si el producto ya existe
            if not Producto.objects.filter(nombre=producto_data['nombre']).exists():
                # Crear el producto
                Producto.objects.create(
                    nombre=producto_data['nombre'],
                    descripcion=producto_data['descripcion'],
                    precio=producto_data['precio'],
                    cantidad_stock=producto_data['cantidad_stock']
                )
                productos_creados += 1
                self.stdout.write(f'✓ Producto creado: {producto_data["nombre"]}')
            else:
                productos_existentes += 1
                self.stdout.write(f'- Producto ya existe: {producto_data["nombre"]}')

        # Resumen final
        self.stdout.write('\n' + '='*50)
        self.stdout.write(self.style.SUCCESS(f'RESUMEN DE CARGA DE PRODUCTOS'))
        self.stdout.write(f'Productos creados: {productos_creados}')
        self.stdout.write(f'Productos ya existentes: {productos_existentes}')
        self.stdout.write(f'Total procesados: {len(productos_data)}')
        self.stdout.write('='*50)

        if productos_creados > 0:
            self.stdout.write(self.style.SUCCESS(f'¡Se han cargado {productos_creados} productos exitosamente!'))
        else:
            self.stdout.write(self.style.WARNING('No se crearon productos nuevos. Todos ya existían en la base de datos.'))