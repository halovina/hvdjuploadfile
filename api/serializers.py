from rest_framework import serializers

class UploadFileSerializer(serializers.Serializer):
    files = serializers.ImageField() 