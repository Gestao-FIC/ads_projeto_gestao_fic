from django.db import models
from sgset.models.matricula_model import MatriculaModel

class QuorumModel(models.Model):
    matricula = models.OneToOneField(MatriculaModel, on_delete=models.CASCADE)
    quorum = models.PositiveIntegerField()

    def __str__(self):
        return f'Quorum para {self.matricula.curso.nome}'
