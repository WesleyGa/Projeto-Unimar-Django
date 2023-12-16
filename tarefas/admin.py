
from django.contrib import admin
from .models import Funcionario, Tarefa

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo')

class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'atribuida_a', 'concluida')

admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Tarefa, TarefaAdmin)