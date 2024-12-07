from django.test import TestCase
from sgset.models import CourseModel
from sgset.serializers.course_serializer import CourseSerializer

class CourseSerializerTest(TestCase):

    def setUp(self):
        # Dados de exemplo para o curso
        self.course_data = {
            'name': 'Introduction to Python',
            'price_per_student': 100.0
        }

    def test_valid_data(self):
        """
        Testa o serializer com dados válidos.
        """
        serializer = CourseSerializer(data=self.course_data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        
        # Verificar os dados validados
        course_instance = serializer.save()
        self.assertEqual(course_instance.name, self.course_data['name'])
        self.assertEqual(course_instance.price_per_student, self.course_data['price_per_student'])

    def test_missing_name(self):
        """
        Testa o serializer quando o campo 'name' está faltando.
        """
        data = self.course_data.copy()
        del data['name']  # Remove o campo 'name' para testar a ausência

        serializer = CourseSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors)

    def test_missing_price_per_student(self):
        """
        Testa o serializer quando o campo 'price_per_student' está faltando.
        """
        data = self.course_data.copy()
        del data['price_per_student']  # Remove o campo 'price_per_student' para testar a ausência

        serializer = CourseSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('price_per_student', serializer.errors)

    def test_invalid_price_per_student(self):
        """
        Testa o serializer quando o campo 'price_per_student' tem um valor inválido (preço negativo).
        """
        data = self.course_data.copy()
        data['price_per_student'] = -100.0  # Preço inválido (negativo)

        serializer = CourseSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('price_per_student', serializer.errors)
        self.assertEqual(serializer.errors['price_per_student'][0], 'O preço por aluno não pode ser negativo.')

    def test_update_method(self):
        """
        Testa a atualização de um curso existente.
        """
        # Criar uma instância inicial do modelo CourseModel
        course = CourseModel.objects.create(**self.course_data)

        # Dados para atualização
        updated_data = {
            'name': 'Advanced Python',
            'price_per_student': 150.0
        }

        # Atualizar o curso com os novos dados
        serializer = CourseSerializer(course, data=updated_data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        updated_course = serializer.save()

        # Verificar se os dados foram atualizados corretamente
        self.assertEqual(updated_course.name, updated_data['name'])
        self.assertEqual(updated_course.price_per_student, updated_data['price_per_student'])

    def test_invalid_data(self):
        """
        Testa o serializer com dados inválidos (exemplo: campos faltando ou inválidos).
        """
        invalid_data = {
            'name': '',  # Nome vazio
            'price_per_student': ''  # Preço vazio
        }

        serializer = CourseSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors)
        self.assertIn('price_per_student', serializer.errors)
