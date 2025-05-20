from rest_framework import serializers

class KYCSerializer(serializers.Serializer):
    id_document = serializers.ImageField()
    selfie = serializers.ImageField()
    id_number_input = serializers.CharField(max_length=50)
