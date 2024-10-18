import uuid
from django.db import models

class Event(models.Model):
    """
    Model to represent date reservations.

    This class allows the registration of date intervals with a description, 
    title, and a tag for categorization, such as holiday, extended holiday, or others.

    Attributes:
        id (AutoField): Auto-incremented primary key for each reservation.
        title (CharField): Title of the reservation (e.g., 'National Holiday').
        description (TextField): Optional description for the reservation.
        start_date (DateField): Start date of the reserved period.
        end_date (DateField): End date of the reserved period.
        tag (CharField): Category of the reservation, with predefined choices 
                         ('holiday', 'extended', 'other').

    Meta:
        ordering: Sets the default ordering of reservations by the start_date.
        verbose_name: User-friendly name for the model.
        verbose_name_plural: User-friendly plural name for the model.

    Methods:
        __str__: Returns a readable string representation of the object.
    """

    TAG_CHOICES = [
        ('feriado', 'Feriado'),
        ('emenda', 'Emenda'),
        ('evento', 'Evento'),
        ('curso', 'Curso'),
        ('outros', 'Outros'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, verbose_name='Title')
    description = models.TextField(blank=True, verbose_name='Description')
    start_date = models.DateField(verbose_name='Start Date')
    end_date = models.DateField(verbose_name='End Date')
    tag = models.CharField(
        max_length=10,
        choices=TAG_CHOICES,
        verbose_name='Tag'
    )

    class Meta:
        verbose_name = 'Date Reservation'
        verbose_name_plural = 'Date Reservations'
        ordering = ['start_date']

    def __str__(self):
        """
        Returns a string representation of the reservation, showing the title 
        and the date interval.
        """
        return f"{self.title} ({self.start_date} - {self.end_date})"
