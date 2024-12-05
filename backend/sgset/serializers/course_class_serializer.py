from rest_framework import serializers
from ..models.course_class import CourseClassModel


class CourseClassModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseClassModel
        fields = '__all__'
