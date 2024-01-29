from rest_framework import serializers

from API.models import *


class BlackjackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users

        fields = ("name", "email", "password_hash")
