from django.shortcuts import render, redirect
from .models import Insidencia

def lista_insidencias(request):
    insidencias = Insidencia.objects.all()
    return render(request, 'insidencia/inicio.html', {'insidencias': insidencias})

def cambiar_estado(request, id):
    insidencias = Insidencia.objects.get(id=id)
    if request.method == 'POST':
        if request.POST.get('accion') == 'completar':
            insidencias.estado = 'completada'
        elif request.POST.get('accion') == 'cancelar':
            insidencias.estado = 'pendiente'
        insidencias.save()
    return redirect('lista_insidencias')

def crear_incidencia(request):
    if request.method == 'POST':
        form = IncidenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_incidencias')  # Redirige a la lista de incidencias después de guardar
    else:
        form = IncidenciaForm()

    return render(request, 'crear_incidencia.html', {'form': form})

def editar_banco(request, id_banco):
    # Obtener el objeto del banco o devolver un 404 si no existe
    banco = get_object_or_404(Banco, id=id_banco)

    if request.method == 'POST':
        # Usamos un formulario basado en el modelo
        form = BankForm(request.POST, instance=banco)
        insidencias = Insidencia.objects.all()
        if form.is_valid():
            form.save()  # Guardamos el banco editado
            return redirect(request,'banco.html',{'insidencias':insidencias})  # Redirigir a la lista de bancos (puedes cambiar esta URL)
    else:
        form = BancoForm(instance=banco)

    return render(request, 'editar_banco.html', {'form': form, 'banco': banco})

# Vista para eliminar un banco
def eliminar_banco(request, id_banco):
    banco = get_object_or_404(Banco, id=id_banco)
    if request.method == 'POST':
        banco.delete()  # Elimina el banco
        return redirect('lista_bancos')  # Redirigir a la lista de bancos

    return render(request, 'eliminar_banco.html', {'banco': banco})