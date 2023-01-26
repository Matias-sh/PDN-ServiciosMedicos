from django.shortcuts import render, redirect
from .forms import *

# Create your views here.

def vista_pacientes(request):
    pacientes = Pacientes.objects.all()
    context = {
        'pacientes': pacientes
    }
    return render(request, 'pacientes/pacientes.html', context)

def vista_crear_paciente(request):
    if request.method == 'POST':
        form = FormPaciente(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vista_pacientes')
    else:
        form = FormPaciente()

    context = {
        'form': form
    }

    return render(request, 'pacientes/nuevo_paciente.html', context)

def vista_editar_paciente(request, id):
    paciente = Pacientes.objects.get(id_paciente=id)
    if request.method == 'POST':
        form = FormPaciente(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('vista_pacientes')
    else:
        form = FormPaciente(instance=paciente)

    context = {
        'form': form
    }

    return render(request, 'pacientes/editar_paciente.html', context)

def vista_eliminar_paciente(request, id):
    paciente = Pacientes.objects.get(id_paciente = id)
    paciente.delete()
    return redirect('vista_pacientes')