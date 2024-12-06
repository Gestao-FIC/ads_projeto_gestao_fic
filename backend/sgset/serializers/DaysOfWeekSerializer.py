from rest_framework import serializers
from sgset.models import DayOfWeekModel


class DaysOfWeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayOfWeekModel
        fields = '__all__'
