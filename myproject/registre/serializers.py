from rest_framework import serializers
from registre.models import Registre


class RegistreSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    User_Name = serializers.CharField(max_length=100)
    Email = serializers.EmailField()
    Contect_No = serializers.IntegerField()
    address = serializers.CharField()    

    def create(self, validated_data):
        """
        Create and return a new `Sign_up` instance, given the validated data.
        """
        return Registre.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Sign_up` instance, given the validated data.
        """
        instance.User_Name = validated_data.get('User_Name', instance.User_Name)
        instance.Email = validated_data.get('Email', instance.Email)
        instance.Contect_No = validated_data.get('Contect_No', instance.Contect_No)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance
# class Sign_upSerealizer(serializers.ModelSerializer):
#     class Meta:
#         model = Sign_up
#         fields = "__all__"