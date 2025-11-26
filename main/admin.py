from django.contrib import admin
from main.models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'usuario','data_limite', 'atualizado_em',)
    list_filter = ('concluida', 'prioridade',)
    search_fields = ('titulo',)


