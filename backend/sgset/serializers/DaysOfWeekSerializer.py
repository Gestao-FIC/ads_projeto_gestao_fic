from rest_framework import serializers
from sgset.models import DayOfWeek


class DaysOfWeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayOfWeek
        fields = '__all__'
