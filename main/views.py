from django.shortcuts import render
from main.models import Task                                        

def task_list(request):
    tarefas = Task.objects.all()
    context = {
        "tarefas": tarefas,
        "titulos_pagina": 'Minhas Tarefas'
    }
    return render(request, 'tasks/task_list.html', context)
