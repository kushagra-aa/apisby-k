from rest_framework import serializers


class TestSerializer(serializers.Serializer):
    Name = serializers.CharField(required=True)

    class Meta:
        fields = '__all__'
