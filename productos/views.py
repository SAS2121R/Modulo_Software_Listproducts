from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Producto
from .forms import ProductoForm


@login_required(login_url='/usuarios/')
def lista_productos(request):
   productos_list = Producto.objects.all().order_by('-fecha_ultima_modificacion')
   paginator = Paginator(productos_list, 10)
   page = request.GET.get('page', 1)
   try:
       productos = paginator.page(page)
   except (PageNotAnInteger, EmptyPage):
       productos = paginator.page(1)
   return render(request, 'productos/product_list.html', {'productos': productos})


@login_required(login_url='/usuarios/')
def create_product(request):
   form = ProductoForm(request.POST or None)
   if request.method == 'POST' and form.is_valid():
       form.save()
       return redirect('productos:lista')
   return render(request, 'productos/product_form.html', {'form': form})


@login_required(login_url='/usuarios/')
def edit_product(request, pk):
   prod = get_object_or_404(Producto, pk=pk)
   form = ProductoForm(request.POST or None, instance=prod)
   if request.method == 'POST' and form.is_valid():
       form.save()
       return redirect('productos:lista')
   return render(request, 'productos/product_form.html', {'form': form})


@login_required(login_url='/usuarios/')
def delete_product(request, pk):
   prod = get_object_or_404(Producto, pk=pk)
   if request.method == 'POST':
       prod.delete()
       return redirect('productos:lista')
   return render(request, 'productos/product_confirm_delete.html', {'producto': prod})

@login_required(login_url='/usuarios/')
def inicio(request):
   """Vista para la página de inicio de productos - requiere autenticación."""
   context = {
       'tienda': 'huellitas_alegres',
       'descripcion': 'Venta de productos para clinica veterinaria',
       'usuario': request.user
   }
   return render(request, 'inicio.html', context)