from django import forms
from .models import Analisis, Paciente ,Doctor

class PacienteForm(forms.ModelForm):
        class Meta:
            model = Paciente
            fields = ('nombre', 'edad',)

class DoctorForm(forms.ModelForm):
        class Meta:
            model = Doctor
            fields = ('nombre', 'especialidad',)

class AnalisisForm(forms.ModelForm):

#todos los campos de Pelicula

    class Meta:
        model = Analisis
        fields = ('nombre', 'costo', 'pacientes')
        

    def __init__ (self, *args, **kwargs):
            super(AnalisisForm, self).__init__(*args, **kwargs)
            self.fields["pacientes"].widget = forms.widgets.CheckboxSelectMultiple()
            self.fields["pacientes"].help_text = "Ingrese pacientes"
            self.fields["pacientes"].queryset = Paciente.objects.all()
