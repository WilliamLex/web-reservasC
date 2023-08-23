from django.contrib import admin

from medicos.models import Carreras, Medico, Agenda

class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ['nome']
    
class MedicoAdmin(admin.ModelAdmin):
    list_display = [
        'nome', 'crm', 'telefone',
    ]
    
class AgendaAdmin(admin.ModelAdmin):
    list_display = [
        'dia', 'medico', 'horario'
    ]
    
admin.site.register(Carreras, EspecialidadeAdmin)
admin.site.register(Medico, MedicoAdmin)
admin.site.register(Agenda, AgendaAdmin)