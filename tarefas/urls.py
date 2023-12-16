from django.urls import path
from .views import tarefa_list, criar_funcionario, funcionario_list, criar_tarefa, index, remover_funcionario, modificar_funcionario,buscar_funcionarios,detalhes_funcionario, editar_tarefa,detalhes_tarefa, remover_tarefa


urlpatterns = [
    path('', index, name='index'),
    path('list', tarefa_list, name='tarefa_list'),
    path('criar/', criar_tarefa, name='criar_tarefa'),
    path('funcionarios/', funcionario_list, name='funcionario_list'),
    path('funcionarios/criar/', criar_funcionario, name='criar_funcionario'),
    path('remover_funcionario/<int:funcionario_id>/', remover_funcionario, name='remover_funcionario'),
    path('modificar_funcionario/<int:funcionario_id>/', modificar_funcionario, name='modificar_funcionario'),
    path('funcionarios/buscar/', buscar_funcionarios, name='buscar_funcionarios'),
    path('detalhes_funcionario/<int:funcionario_id>/', detalhes_funcionario, name='detalhes_funcionario'),
    path('editar_tarefa/<int:tarefa_id>/', editar_tarefa, name='editar_tarefa'),
    path('detalhes_tarefa/<int:tarefa_id>/', detalhes_tarefa, name='detalhes_tarefa'),
    path('remover_tarefa/<int:tarefa_id>/', remover_tarefa, name='remover_tarefa'),
]