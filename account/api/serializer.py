from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    confirm_password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ['email','name','password','confirm_password']

    # veryfi password 

    def validate(self, attrs):
        password =attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError("password and confirm_password doesn't match.")
        return attrs
    
    # Email veryfi :-

    def Validate_email(self , value ):
        if User .objects .filter(email = value).exists():
            raise serializers.ValidationError("user with this email already exists.")
        return value
    
    # create data :-

    def create(self,validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password'],
        )
        user.is_active = False
        user.save()
        return user
    
