from rest_framework import serializers
from sgset.models import CourseModel
from ..models.course import Course

class CourseSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, required=True)
    price_per_student = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)

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
