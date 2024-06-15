from rest_framework import serializers

class QuerySerializer(serializers.Serializer):
    query = serializers.CharField()

class UserDataSerializer(serializers.Serializer):
    age = serializers.CharField()
    weight = serializers.CharField()
    medical_history = serializers.CharField()