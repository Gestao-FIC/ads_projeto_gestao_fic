from django.db import models
from sgset.models.curso_model import CursoModel
from sgset.models.docente_model import DocenteModel

class MatriculaModel(models.Model):
    curso = models.ForeignKey(CursoModel, on_delete=models.CASCADE)
    docente = models.ForeignKey(DocenteModel, on_delete=models.CASCADE)
    numero_estudantes_estimados = models.PositiveIntegerField()
    numero_estudantes_realizados = models.PositiveIntegerField()

    def __str__(self):
        return f'Matrícula para {self.curso.nome}'
