from rest_framework import serializers
from sgset.models.class_schedule import ClassSchedule


class ClassScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassSchedule
        fields = '__all__'
