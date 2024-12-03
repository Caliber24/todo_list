from rest_framework import serializers
from .models import Task
from django.utils import timezone

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "name",'created_at', 'updated_at', 'description', 'task_group', 'start_date', 'end_date', 'is_complete']

    def create(self, validated_data):
        validated_data.pop('is_complete', None)
        return super().create(validated_data)
    
    def validate(self, attrs):
        if attrs['start_date'] < timezone.now():
            raise serializers.ValidationError({'start_date':["Start date cannot be in the past."]})
        elif attrs['end_date'] < timezone.now():
            raise serializers.ValidationError({"end_date":['End date cannot be in the past.']})
        elif attrs['start_date'] >= attrs['end_date']:
            raise serializers.ValidationError({"end_date":["End date must be after start date."]})
        else:
            return attrs