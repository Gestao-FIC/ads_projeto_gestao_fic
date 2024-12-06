from django.test import TestCase
from rest_framework.exceptions import ValidationError
from sgset.serializers.auth_serializer import AuthSerializer

class AuthSerializerTest(TestCase):
    def test_valid_data(self):
        """
        Testa o serializer com dados válidos.
        """
        data = {
            'username': 'john_doe',
            'password': 'secure_password123'
        }
        serializer = AuthSerializer(data=data)
        
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['username'], 'john_doe')
        self.assertEqual(serializer.validated_data['password'], 'secure_password123')

    def test_missing_username(self):
        """
        Testa o serializer sem o campo 'username'.
        """
        data = {
            'password': 'secure_password123'
        }
        serializer = AuthSerializer(data=data)
        
        self.assertFalse(serializer.is_valid())
        self.assertIn('username', serializer.errors)

    def test_missing_password(self):
        """
        Testa o serializer sem o campo 'password'.
        """
        data = {
            'username': 'john_doe'
        }
        serializer = AuthSerializer(data=data)
        
        self.assertFalse(serializer.is_valid())
        self.assertIn('password', serializer.errors)

    def test_empty_fields(self):
        """
        Testa o serializer com campos vazios.
        """
        data = {
            'username': '',
            'password': ''
        }
        serializer = AuthSerializer(data=data)
        
        self.assertFalse(serializer.is_valid())
        self.assertIn('username', serializer.errors)
        self.assertIn('password', serializer.errors)
