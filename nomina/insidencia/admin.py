from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from .models import Insidencia, Banco, Venta
from .forms import BancoForm
from django.utils.html import format_html

@admin.register(Insidencia)
class InsidenciaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'estado')

    # Personalizar la vista de cambio
    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_buttons'] = True  # Pasar contexto para mostrar los botones personalizados
        return super().change_view(request, object_id, form_url, extra_context=extra_context)

    # Agregar botones personalizados
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:id>/completar/', self.admin_site.admin_view(self.completar_insidencia), name='completar_insidencia'),
            path('<int:id>/cancelar/', self.admin_site.admin_view(self.cancelar_insidencia), name='cancelar_insidencia'),
        ]
        return custom_urls + urls

    def completar_insidencia(self, request, id):
        insidencia = Insidencia.objects.get(pk=id)
        insidencia.estado = 'completado'
        insidencia.save()
        self.message_user(request, "La incidencia ha sido completada.")
        return redirect('admin:app_incidencia_change', id)

    def cancelar_insidencia(self, request, id):
        insidencia = Insidencia.objects.get(pk=id)
        insidencia.estado = 'pendiente'
        insidencia.save()
        self.message_user(request, "La incidencia ha sido marcada como pendiente.")
        return redirect('admin:app_incidencia_change', id)

class BancoAdmin(admin.ModelAdmin):
    form = BancoForm
    list_display = ('nombre', 'imagen', 'status1','status2','custom1')

class VentaAdmin(admin.ModelAdmin):
    change_form_template = 'templates/insidencia/change_form.html'
    list_display = ('total_ventas', 'total_ganancias', 'porcentaje_ganancias')
    def mostrar_barra_estado(self, obj):
        if obj.estado == 'nuevo':
            color = 'red'
            texto = 'Nuevo'
        elif obj.estado == 'procesando':
            color = 'orange'
            texto = 'Procesando'
        elif obj.estado == 'completado':
            color = 'green'
            texto = 'Completado'
        else:
            color = 'gray'
            texto = 'Cancelado'
        
        return format_html('<div style="width: 100px; background-color: {}; color: white; text-align: center;">{}</div>', color, texto)
    
    mostrar_barra_estado.short_description = 'Estado'

admin.site.register(Banco, BancoAdmin)

admin.site.register(Venta, VentaAdmin)