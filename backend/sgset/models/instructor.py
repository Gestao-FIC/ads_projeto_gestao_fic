import uuid
from django.db import models


class Instructor(models.Model):
    """
    Represents a teacher or instructor responsible for classes.

    Attributes:
        id (UUIDField): Unique identifier for the instructor (primary key).
        name (CharField): Name of the instructor.
        source (CharField): Indicates the origin of the instructor, with options 
                            such as 'SGSET' or 'User'.
    """

    SOURCE_CHOICES = [
        ('sgset', 'SGSET'),
        ('user', 'User'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, verbose_name='Instructor Name')
    source = models.CharField(
        max_length=10, choices=SOURCE_CHOICES, verbose_name='Source')

    class Meta:
        verbose_name = 'Instructor'
        verbose_name_plural = 'Instructors'
        ordering = ['name']

    def __str__(self) -> str:
        """
        Returns a string representation of the instructor.

        Returns:
            str: The name of the instructor.
        """
        return self.name
