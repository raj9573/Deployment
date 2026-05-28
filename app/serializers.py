from rest_framework import serializers




class ResponseSerializer(serializers.Serializer):
    error = serializers.BooleanField(default=False)
    message = serializers.CharField()