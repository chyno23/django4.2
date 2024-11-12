# forms.py
from django import forms
from .models import Insidencia, Banco

class IncidenciaForm(forms.ModelForm):
    class Meta:
        model = Insidencia
        fields = ['titulo', 'estado']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',  # Clase CSS para bootstrap
                'placeholder': 'Escribe el título de la incidencia'
            }),

            'estado': forms.Select(attrs={
                'class': 'form-select',  # Clase CSS para bootstrap
            })
        }
    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if 'spam' in titulo:
            raise forms.ValidationError("El título no puede contener la palabra 'spam'.")
        return titulo

class BancoForm(forms.ModelForm):
    class Meta:
        model = Banco
        fields = ['nombre', 'imagen', 'status1', 'status2', 'custom1', 'custom2']  # Los campos que tienes en tu modelo Banco