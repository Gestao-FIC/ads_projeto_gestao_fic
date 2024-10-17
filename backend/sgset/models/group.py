import uuid
from django.db import models
from .course import Course
from .teacher import Teacher

class Group(models.Model):
    """Represents a specific class within a course.

    Attributes:
        id (UUIDField): Unique identifier for the class (primary key).
        course (ForeignKey): Reference to the related course.
        teacher (ForeignKey): Reference to the teacher responsible for the class.
        code (CharField): Code identifying the class (e.g., 'CQ.AJUS.N-1').
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
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='classes')
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='classes')
    code = models.CharField(max_length=20, unique=True)
    shift = models.CharField(max_length=20)
    modality = models.CharField(max_length=50)
    period_from = models.DateField()
    period_to = models.DateField()
    attendance = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()
    estimated_enrollments = models.IntegerField()
    actual_enrollments = models.IntegerField()
    quorum = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        """Returns a string representation of the class.

        Returns:
            str: A string combining the class code and course name.
        """
        return f'{self.code} - {self.course.name}'