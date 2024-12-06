from rest_framework import serializers
from ..models.course_class import CourseClass

class UpdateQuorumSerializer(serializers.Serializer):
    quorum = serializers.IntegerField(
        required=True,
        min_value=0,
        help_text="The new quorum value. Must be a positive integer."
    )

    def update(self, instance, validated_data):
        """
        Update the quorum field in the CourseClassModel instance.
        """
        instance.quorum = validated_data.get('quorum', instance.quorum)
        instance.save()
        return instance
