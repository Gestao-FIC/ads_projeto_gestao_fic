from django.db import models
from .instructor import Instructor
from .course_class import CourseClass


class InstructorClass(models.Model):
    """
    Represents the relationship between an instructor and a course class.

    Fields:
        instructor (ForeignKey): Reference to the instructor.
        course_class (ForeignKey): Reference to the course.
    """

    instructor = models.ForeignKey(
        Instructor, on_delete=models.CASCADE, related_name='courses'
    )
    course_class = models.ForeignKey(
        CourseClass, on_delete=models.CASCADE, related_name='instructors'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['instructor', 'course_class'], name='unique_instructor_class'
            )
        ]
        verbose_name = 'Instructor Class'
        verbose_name_plural = 'Instructor Class'
        ordering = ['instructor', 'course_class']

    def __str__(self) -> str:
        """
        Returns a string representation of the instructor-course relationship.

        Returns:
            str: The instructor name and course name.
        """
        return f"{self.instructor.name} - {self.course_class.code}"
