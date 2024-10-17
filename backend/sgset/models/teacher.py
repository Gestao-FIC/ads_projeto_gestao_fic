import uuid
from django.db import models

class Teacher(models.Model):
    """Represents a teacher or instructor responsible for classes.

    Attributes:
        id (UUIDField): Unique identifier for the teacher (primary key).
        name (CharField): Name of the teacher.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        """Returns a string representation of the teacher.

        Returns:
            str: The name of the teacher.
        """
        return self.name