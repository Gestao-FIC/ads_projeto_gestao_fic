from rest_framework import serializers
from sgset.models.class_schedule import ClassScheduleModel


class ClassScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassScheduleModel
        fields = '__all__'
