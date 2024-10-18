from django.db import models
from .course import Course


class CourseClass(models.Model):
    """
    Represents a specific class within a course.

    Attributes:
        code (CharField): Unique code identifying the class (primary key, e.g., 'CQ.AJUS.N-1').
        course (ForeignKey): Reference to the related course.
        shift (CharField): Time of day when the class occurs (e.g., 'Evening').
        modality (CharField): Type or modality of the class (e.g., 'In-person').
        period_from (DateField): Start date of the class period.
        period_to (DateField): End date of the class period.
        attendance (CharField): Place or form of attendance (e.g., 'School').
        start_time (TimeField): Class start time.
        end_time (TimeField): Class end time.
        estimated_enrollments (IntegerField): Estimated number of students.
        actual_enrollments (IntegerField): Actual number of students enrolled.
        quorum (IntegerField): Minimum number of students required (optional).
        status (CharField): Current status of the class with predefined choices.
        income (DecimalField): Total income from all enrollments (optional).
    """

    STATUS_CHOICES = [
        ('programado', 'Programado'),
        ('em_andamento', 'Em andamento'),
        ('concluido', 'Concluído'),
        ('cancelado', 'Cancelado'),
    ]

    code = models.CharField(
        primary_key=True, max_length=20, verbose_name='Class Code')
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='classes', verbose_name='Course'
    )
    shift = models.CharField(null=True, max_length=20, verbose_name='Shift')
    duration = models.IntegerField(
        null=True, verbose_name='Duration')
    modality = models.CharField(
        max_length=50, null=True, verbose_name='Modality')
    attendance = models.CharField(
        max_length=50, null=True, verbose_name='Attendance')
    period_from = models.DateField(null=True, verbose_name='Start Date')
    period_to = models.DateField(null=True, verbose_name='End Date')
    start_time = models.TimeField(null=True, verbose_name='Start Time')
    end_time = models.TimeField(null=True, verbose_name='End Time')
    estimated_enrollments = models.IntegerField(
        null=True, verbose_name='Estimated Enrollments')
    actual_enrollments = models.IntegerField(
        null=True, verbose_name='Actual Enrollments')
    quorum = models.IntegerField(
        null=True, blank=True, verbose_name='Minimum Quorum'
    )
    status = models.CharField(
        max_length=12,
        choices=STATUS_CHOICES,
        verbose_name='Progress Status'
    )
    income = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        verbose_name='Income from Enrollments'
    )

    class Meta:
        verbose_name = 'Course Class'
        verbose_name_plural = 'Course Classes'
        ordering = ['period_from', 'start_time']

    def __str__(self) -> str:
        """
        Returns a string representation of the class.

        Returns:
            str: A string combining the class code and course name.
        """
        return f'{self.code} - {self.course.name}'
