import uuid
from django.db import models
from backend.sgset.models.course_class import Group
from sgset.models.day_of_week import DayOfWeek


class ClassSchedule(models.Model):
    """Represents a specific class schedule for a given day of the week.

    Attributes:
        id (UUIDField): Unique identifier for the schedule entry (primary key).
        class_instance (ForeignKey): Reference to the related class.
        day_of_week (ForeignKey): Reference to the corresponding day of the week.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    class_instance = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='day_schedules')
    day_of_week = models.ForeignKey(DayOfWeek, on_delete=models.CASCADE, related_name='class_schedules')

    def __str__(self) -> str:
        """Returns a string representation of the class schedule.

        Returns:
            str: A string combining the class code and day of the week.
        """
        return f'{self.class_instance} - {self.day_of_week.name}'