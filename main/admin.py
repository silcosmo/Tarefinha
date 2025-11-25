from django.contrib import admin
from main.models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'usuario','atualizado_em',)
    list_filter = ('concluidas', 'prioridade',)
    search_fields = ('titulo',)


