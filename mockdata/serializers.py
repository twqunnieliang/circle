from rest_framework import serializers
from .models import MockAPI
import json

class MockAPISerializer(serializers.ModelSerializer):
    mock_data = serializers.SerializerMethodField()

    def get_mock_data(self, obj):
        if isinstance(obj.mock_data, str):
            return json.loads(obj.mock_data)
        return obj.mock_data 

    class Meta:
        model = MockAPI
        fields = '__all__'
