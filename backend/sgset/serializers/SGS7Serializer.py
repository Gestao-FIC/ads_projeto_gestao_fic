from rest_framework import serializers
from sgset.models import SGSETModel

class SGSETSerializer(serializers.ModelSerializer):
    class Meta:
        model = SGSETModel
        fields = '__all__'