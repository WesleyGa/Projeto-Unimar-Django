from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    SIM = True
    NAO = False

    SIM_NAO_CHOICES = [
        (SIM, 'Sim'),
        (NAO, 'Não'),
    ]

    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    atribuida_a = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    concluida = models.BooleanField(default=NAO, choices=SIM_NAO_CHOICES)

    def __str__(self):
        return self.titulo
