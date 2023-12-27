from rest_framework import serializers

from API.models import TestModel


class BlackjackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = ('title', 'content')