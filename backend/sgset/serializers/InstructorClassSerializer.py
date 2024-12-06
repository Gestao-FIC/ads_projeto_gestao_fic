from rest_framework import serializers
from sgset.models import Instructor

class InstructorClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'