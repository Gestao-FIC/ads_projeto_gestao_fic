import uuid
from django.db import models

class DayOfWeek(models.Model):
    """Represents a day of the week (e.g., 'Monday', 'Tuesday').

    Attributes:
        id (UUIDField): Unique identifier for the day (primary key).
        name (CharField): Name of the day (e.g., 'Monday').
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        """Returns a string representation of the day of the week.

        Returns:
            str: The name of the day.
        """
        return self.name