from rest_framework import serializers
from sgset.repositories.GoalRepository import GoalModel

class GoalSerializer(serializers.ModelSerializer):
    """
    Serializer for the GoalModel.
    Serializes and validates input/output data for goals.
    """

    class Meta:
        model = GoalModel
        fields = ['id', 'year', 'goal_description', 'value']
        read_only_fields = ['id']
    
    def validate_year(self, value):
        """
        Validate that the year is not in the past.
        """
        from datetime import datetime
        current_year = datetime.now().year
        if value < current_year:
            raise serializers.ValidationError("Year cannot be in the past.")
        return value

    def validate_value(self, value):
        """
        Validate that the value is positive.
        """
        if value <= 0:
            raise serializers.ValidationError("Value must be positive.")
        return value
