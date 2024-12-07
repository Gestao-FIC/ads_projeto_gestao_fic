import uuid
from django.db import models


class SGSETModel(models.Model):
    """Model to represent the data that comes from sgse7 as a backup

    Attributes:
        id (UUIDField): Unique identifier for each course.
        course_name (CharField): Name of the course.
        class_name (CharField): Name or code of the class (default "000000").
        situation (CharField): Current status of the course (e.g., 'Concluída').
        shift (CharField): The shift when the course is held (e.g., 'Vespertino').
        workload (IntegerField): Total hours of the course.
        actual_enrollment (IntegerField): Number of actual enrollments.
        estimated_enrollment (IntegerField): Estimated number of enrollments.
        start_date (DateTimeField): Start date and time of the course.
        end_date (DateTimeField): End date and time of the course.
        start_time (TimeField): Time the course starts.
        end_time (TimeField): Time the course ends.
        week_days (CharField): Days of the week the course occurs.
        modality (CharField): Type of modality for the course.
        city (CharField): City where the course is held.
        service (CharField): Type of service (e.g., 'Escola').
        price_per_participant (CharField): Price per participant in string format.
        value (DecimalField): The numeric value of the price per participant.

    Meta:
        ordering: Sets the default ordering of courses by start_date.
        verbose_name: User-friendly name for the model.
        verbose_name_plural: User-friendly plural name for the model.

    Methods:
        __str__: Returns a readable string representation of the course.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    curso = models.CharField(max_length=255, blank=True, null=True, verbose_name='Course Name')
    turma = models.CharField(max_length=100, default='000000', blank=True, verbose_name='Class')
    situacao = models.CharField(max_length=50, blank=True, null=True, verbose_name='Situation')
    turno = models.CharField(max_length=20, blank=True, null=True, verbose_name='Shift')
    carga_horaria = models.IntegerField(blank=True, null=True, verbose_name='Workload (hours)')
    no_de_matriculas_realizado = models.IntegerField(blank=True, null=True, verbose_name='Actual Enrollment')
    no_de_matriculas_estimado = models.IntegerField(blank=True, null=True, verbose_name='Estimated Enrollment')
    periodo_de = models.DateTimeField(blank=True, null=True, verbose_name='Start Date')
    periodo_ate = models.DateTimeField(blank=True, null=True, verbose_name='End Date')
    horario_de = models.TimeField(blank=True, null=True, verbose_name='Start Time')
    horario_ate = models.TimeField(blank=True, null=True, verbose_name='End Time')
    dia_da_semana = models.CharField(max_length=255, blank=True, null=True, verbose_name='Days of the Week')
    modalidade = models.CharField(max_length=100, blank=True, null=True, verbose_name='Modality')
    municipio = models.CharField(max_length=100, blank=True, null=True, verbose_name='City')
    atendimento = models.CharField(max_length=100, blank=True, null=True, verbose_name='Service Type')
    preco_por_participante = models.CharField(max_length=50, blank=True, null=True, verbose_name='Price per Participant')
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Value')

    class Meta:
        ordering = ['periodo_de']

    def __str__(self):
        """
        Returns a string representation of the course, showing the course name
        and the date interval.
        """
        return f"{self.curso or 'SEM CÓDIGO DA TURMA'} ({self.periodo_de} - {self.periodo_ate})"
