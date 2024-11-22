import uuid
from django.db import models


class Goal(models.Model):
    """
    Model to represent goals for specific years.

    This class allows the registration of goals with a specific year, value, 
    and category (course, enrollments, or revenue).

    Attributes:
        id (AutoField): Auto-incremented primary key for each goal.
        year (IntegerField): Year the goal refers to (e.g., 2024).
        value (DecimalField): Target value for the goal.
        goal_type (CharField): Type of the goal, with predefined choices 
                              ('course', 'enrollments', 'revenue').

    Meta:
        ordering: Sets the default ordering of goals by year.
        verbose_name: User-friendly name for the model.
        verbose_name_plural: User-friendly plural name for the model.

    Methods:
        __str__: Returns a readable string representation of the object.
    """

    GOAL_CHOICES = [
        ('cursos', 'Cursos'),
        ('matriculas', 'Matriculas'),
        ('receita', 'Receita'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    year = models.IntegerField(verbose_name='Year')
    goal_description = models.CharField(
        max_length=12,
        choices=GOAL_CHOICES,
        verbose_name='Goal Type'
    )
    value = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Value')

    class Meta:
        verbose_name = 'Goal'
        verbose_name_plural = 'Goals'
        ordering = ['year']

    def __str__(self):
        """
        Returns a string representation of the goal, showing the year, 
        goal type, and value.
        """
        return f"{self.year} - {self.goal_type}: {self.value}"
