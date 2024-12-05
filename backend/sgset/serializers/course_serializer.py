from rest_framework import serializers
from ..models.course import CourseModel

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = ['id', 'name', 'price_per_student']
