from django.test import TestCase
from sgset.models.instructor import Instructor
from sgset.models.class_schedule import CourseClassModel
from sgset.models import InstructorClass
from sgset.models.course import CourseModel

class InstructorClassModelTest(TestCase):
    def setUp(self):
        """
        Configura os dados necessários para o teste.
        """
        self.instructor = Instructor.objects.create(name='John Doe', source='sgset')
        self.course = CourseModel.objects.create(name='Computer Science')
        self.course_class = CourseClassModel.objects.create(code='CS101', course=self.course)
        self.instructor_class = InstructorClass.objects.create(
            instructor=self.instructor,
            course_class=self.course_class
        )

    def test_str_method(self):
        """
        Testa o método __str__ do modelo InstructorClass.
        """
        expected_str = f"{self.instructor.name} - {self.course_class.code}"
        self.assertEqual(str(self.instructor_class), expected_str)

    def test_unique_constraint(self):
        """
        Testa a restrição de unicidade entre instructor e course_class.
        """
        with self.assertRaises(Exception):
            InstructorClass.objects.create(
                instructor=self.instructor,
                course_class=self.course_class
            )
