from django.test import TestCase
from sgset.models import InstructorClass, Instructor, CourseClass, Course


class InstructorClassModelTest(TestCase):
    def setUp(self):
        """
        Configura os dados necessários para o teste.
        """
        self.instructor = Instructor.objects.create(name='John Doe')
        self.course = Course.objects.create(
            name='Computer Science')  # Criar o curso
        self.course_class = CourseClass.objects.create(
            code='CS101', course=self.course)  # Atribuindo o curso
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
