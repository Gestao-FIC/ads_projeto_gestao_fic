from django.db import models

class CursoModel(models.Model):
    nome = models.CharField(max_length=100)
    turma = models.CharField(max_length=50)
    turno = models.CharField(max_length=50)
    modalidade = models.CharField(max_length=50)
    periodo_de = models.DateField()
    periodo_ate = models.DateField()
    atendimento = models.CharField(max_length=50)
    horario_de = models.TimeField()
    horario_ate = models.TimeField()

    def __str__(self):
        return self.nome
