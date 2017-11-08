from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required

#librería para manejar el envío de mensajes

from django.contrib import messages
from .forms import AnalisisForm,PacienteForm,DoctorForm
from consultorio.models import Analisis, Consulta, Paciente,Doctor



# Create your views here.
def paginaprincipal(request):
    return render(request,'consultorio/pagina/index.html')

@login_required
def listar_pacientes(request):
    pa=Paciente.objects.order_by('nombre')
    return render(request,'consultorio/pacientes/index.html',{'pa':pa})
@login_required
def paciente_nuevo(request):
    if request.method == "POST":
        formulario = PacienteForm(request.POST)
        if formulario.is_valid():
            paciente = formulario.save(commit=False)
            paciente.save()
            return redirect('listar_pacientes')
    else:
        formulario = PacienteForm()
    return render(request, 'consultorio/pacientes/paciente_edit.html', {'formulario': formulario})
@login_required
def paciente_edit(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == "POST":
        formulario = PacienteForm(request.POST, instance=paciente)
        if formulario.is_valid():
            paciente = formulario.save(commit=False)
            paciente.save()
            return redirect('listar_pacientes')
    else:
        formulario = PacienteForm(instance=paciente)
    return render(request, 'consultorio/pacientes/paciente_edit.html', {'formulario': formulario})
@login_required
def paciente_remove(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    paciente.delete()
    return redirect('listar_pacientes')
@login_required
def listar_doctores(request):
    doc=Doctor.objects.order_by('nombre')
    return render(request,'consultorio/doctores/index.html',{'doc':doc})
@login_required
def doctor_nuevo(request):
    if request.method == "POST":
        formulario = DoctorForm(request.POST)
        if formulario.is_valid():
            doctor = formulario.save(commit=False)
            doctor.save()
            return redirect('listar_doctores')
    else:
        formulario = DoctorForm()
    return render(request, 'consultorio/doctores/doctor_edit.html', {'formulario': formulario})
@login_required
def doctor_edit(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == "POST":
        formulario = DoctorForm(request.POST, instance=doctor)
        if formulario.is_valid():
            doctor = formulario.save(commit=False)
            doctor.save()
            return redirect('listar_doctores')
    else:
        formulario = DoctorForm(instance=doctor)
    return render(request, 'consultorio/doctores/doctor_edit.html', {'formulario': formulario})
@login_required
def doctor_remove(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    doctor.delete()
    return redirect('listar_doctores')


@login_required
def listar_consultas(request):
    con=Consulta.objects.all()
    return render(request,'consultorio/consultas/index.html',{'con':con})

@login_required
def analisis_nuevo(request):
    if request.method == "POST":
        formulario = AnalisisForm(request.POST)
        if formulario.is_valid():
            analisis = Analisis.objects.create(nombre=formulario.cleaned_data['nombre'], costo = formulario.cleaned_data['costo'])
            for paciente_id in request.POST.getlist('pacientes'):
                consulta = Consulta(paciente_id=paciente_id, analisis_id = analisis.id)
                consulta.save()
                return redirect('listar_consultas')
            messages.add_message(request, messages.SUCCESS, 'Consulta Guardada Exitosamente')
    else:
        formulario = AnalisisForm()
    return render(request, 'consultorio/analisis/analisis_edit.html', {'formulario': formulario})
