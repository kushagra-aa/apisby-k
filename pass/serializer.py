from rest_framework import serializers


class RandomGenratorSerializer(serializers.Serializer):
    """
    Takes Length for the Password
    """
    Length = serializers.CharField(required=True)

    class Meta:
        fields = '__all__'
