from rest_framework import serializers
from .models import Daily


class DailySerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = Daily
        fields = ('id', 'do', 'study', 'review', 'score', 'created_at')