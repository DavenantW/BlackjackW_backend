from rest_framework import serializers


class UsersSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    email = serializers.CharField()
    password_hash = serializers.IntegerField()
    money = serializers.IntegerField()
    games = serializers.IntegerField()
    wins = serializers.IntegerField()
