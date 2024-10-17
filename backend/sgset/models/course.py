import uuid
from django.db import models


class Course(models.Model):
    """Represents a course offered, such as 'Mechanical Fitter' or 'Arduino'. 

    Fields:
        id (UUIDField): Unique identifier for the course (primary key).
        name (CharField): Name of the course.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        """Returns a string representation of the course.

        Returns:
            str: The name of the course.
        """
        return self.name
