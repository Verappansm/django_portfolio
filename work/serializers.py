# serializers.py
from rest_framework import serializers
from .models import WorkExperience

class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ['id', 'title', 'description', 'start_date', 'end_date', 'experience_type']
