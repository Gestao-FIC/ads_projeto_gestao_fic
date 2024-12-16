from rest_framework import serializers
from ..models.course_class import CourseClass


class CourseClassModelSerializer(serializers.ModelSerializer):
    course = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = CourseClass
        fields = '__all__'
