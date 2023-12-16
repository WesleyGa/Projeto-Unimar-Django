from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa, Funcionario
from .forms import TarefaForm, FuncionarioForm
from django.views.decorators.http import require_POST
from django.db.models import Q
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def tarefa_list(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'tarefa_list.html', {'tarefas': tarefas})

def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('tarefa_list')
    else:
        form = TarefaForm()
    return render(request, 'criar_tarefa.html', {'form': form})

def editar_tarefa(request, tarefa_id):

    tarefa = get_object_or_404(Tarefa, id=tarefa_id)

    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('tarefa_list')
    else:
        form = TarefaForm(instance=tarefa)

    return render(request, 'editar_tarefa.html', {'form': form, 'tarefa': tarefa})

def detalhes_tarefa(request, tarefa_id):

    tarefa = get_object_or_404(Tarefa, id=tarefa_id)

    return render(request, 'detalhes_tarefa.html', {'tarefa': tarefa})



def funcionario_list(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'funcionario_list.html', {'funcionarios': funcionarios})

def criar_funcionario(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('funcionario_list')
    else:
        form = FuncionarioForm()

    return render(request, 'criar_funcionario.html', {'form': form})

@require_POST
def remover_funcionario(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, id=funcionario_id)
    funcionario.delete()
    return redirect('funcionario_list')


def buscar_funcionarios(request):
    query = request.GET.get('q')

    if query:
        resultados = Funcionario.objects.filter(
            Q(nome__icontains=query) |  
            Q(cargo__icontains=query)  
        ).distinct()
    else:
        resultados = Funcionario.objects.all()

    return render(request, 'buscar_funcionarios.html', {'resultados': resultados, 'query': query})

def detalhes_funcionario(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, pk=funcionario_id)
    tarefas = funcionario.tarefa_set.all()  
    return render(request, 'detalhes_funcionario.html', {'funcionario': funcionario, 'tarefas': tarefas})



def modificar_funcionario(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, id=funcionario_id)
    
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('funcionario_list')
    else:
        form = FuncionarioForm(instance=funcionario)

    return render(request, 'modificar_funcionario.html', {'form': form, 'funcionario': funcionario})

def remover_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    
    if request.method == 'POST':
       
        tarefa.delete()
       
        return redirect('tarefa_list')
    else:
        
        return JsonResponse({'status': 'error', 'message': 'Método não permitido'})



