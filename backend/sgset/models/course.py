import uuid
from django.db import models


class Course(models.Model):
    """
    Represents a course offered, such as 'Mechanical Fitter' or 'Arduino'.

    Fields:
        id (UUIDField): Unique identifier for the course (primary key).
        name (CharField): Name of the course.
        price_per_student (DecimalField): Price charged per student for this course.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, verbose_name="Course Name")
    price_per_student = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        verbose_name="Price per Student"
    )

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ["name"]

    def __str__(self) -> str:
        """
        Returns a string representation of the course.

        Returns:
            str: The name of the course and its price per student.
        """
        return f"{self.name} - ${self.price_per_student:.2f}"
