from rest_framework import serializers
from .models import Property, Entity


class EntitySerializer(serializers.ModelSerializer):
  value = serializers.IntegerField()
  properties = serializers.StringRelatedField(read_only=True, many=True)

  class Meta:
    model = Entity
    fields = ('__all__')
