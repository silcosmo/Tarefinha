from django.shortcuts import render
from django.views.generic import TempalteView

def task_list(request):
    tarefas = Task.objects.all()
    context = {
        "tarefas": tarefas,
        "titulos_pagina": 'Minhas Tarefas'
    }
    return render(request, 'tasks/task_list.html', context)
