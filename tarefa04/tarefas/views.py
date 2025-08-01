from datetime import date
from django.shortcuts import render
from .models import Tarefa

def lista_tarefas(request):
    hoje = date.today()
    tarefas = Tarefa.objects.all()
    return render(request, 'tarefas/lista_tarefas.html', {
        'tarefas': tarefas,
        'hoje': hoje
    })
