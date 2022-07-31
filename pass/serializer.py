from rest_framework import serializers


class RandomGenratorSerializer(serializers.Serializer):
    """
    Takes 'Length' for the Password
    """
    Length = serializers.CharField(required=True)

    class Meta:
        fields = '__all__'


class RandomWithArgumentsSerializer(serializers.Serializer):
    """
    Takes 'Length' for the Password &
    Boolean Arguments: 'Upper','Lower','Digits','Symbols'
    """
    Length = serializers.CharField(required=True)
    Upper = field_name = serializers.BooleanField(allow_null=False)
    Lower = field_name = serializers.BooleanField(allow_null=False)
    Digits = field_name = serializers.BooleanField(allow_null=False)
    Symbols = field_name = serializers.BooleanField(allow_null=False)

    class Meta:
        fields = '__all__'
