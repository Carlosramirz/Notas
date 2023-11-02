from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Nota

# Lista todas las notas
@login_required
def lista_notas(request):
    notas = Nota.objects.filter(usuario=request.user)
    return render(request, 'notas/lista_notas.html', {'notas': notas})

# Crea nuevas notas
@login_required
def crear_nota(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        contenido = request.POST['contenido']
        Nota.objects.create(titulo=titulo, contenido=contenido, usuario=request.user)
        return redirect('lista_notas')
    return render(request, 'notas/crear_nota.html')

# Editar notas
@login_required
def editar_nota(request, nota_id):
    nota = get_object_or_404(Nota, id=nota_id, usuario=request.user)

    if request.method == 'POST':
        titulo = request.POST['titulo']
        contenido = request.POST['contenido']
        nota.titulo = titulo
        nota.contenido = contenido
        nota.save()
        return redirect('lista_notas')
    return render(request, 'notas/editar_nota.html', {'nota': nota})

@login_required
def eliminar_nota(request, nota_id):
    nota = get_object_or_404(Nota, id=nota_id, usuario=request.user)
    if request.method == 'GET':
        nota.delete()
        return redirect('lista_notas')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("Usuario creado con éxito")
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})   

