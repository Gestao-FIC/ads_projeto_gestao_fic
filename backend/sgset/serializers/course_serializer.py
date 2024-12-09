from rest_framework import serializers
from ..models.course import Course

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['id', 'name', 'price_per_student']

    def validate_price_per_student(self, value):
        """
        Valida que o preço por aluno não seja negativo.
        """
        if value < 0:
            raise serializers.ValidationError("O preço por aluno não pode ser negativo.")
        return value
