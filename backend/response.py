from rest_framework import serializers

# 400
from rest_framework import serializers

class BadRequestExampleSerializer(serializers.Serializer):
    detail = serializers.CharField()