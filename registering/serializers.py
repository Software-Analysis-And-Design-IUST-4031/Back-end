from rest_framework import serializers
from .models import CustomUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ['firstname', 'lastname', 'username', 'password', 'confirm_password', 'email']
        extra_kwargs = {
            'firstname': {'required': True},
            'lastname': {'required': True},
            'username': {'required': True},
            'password': {'write_only': True, 'required': True},
            'email': {'required': True}
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = CustomUser.objects.create_user(
            firstname=validated_data['firstname'],
            lastname=validated_data['lastname'],
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
        )
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 200)
    password = serializers.CharField(max_length = 200, min_length=10, style={'input_type': 'password'})
    token = serializers.CharField(max_length=255, read_only=True)




class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['user_id', 'email', 'firstname', 'lastname', 'username', 'is_active', 'is_admin','date_joined']

 


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['firstname', 'lastname', 'username']
        extra_kwargs = {
            'firstname': {'required': True},
            'lastname': {'required': True},
            'username': {'required': True}
        }









