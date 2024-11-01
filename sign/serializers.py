from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=200, min_length = 10, style={'input_type': 'password'})
    class Meta:
        model = get_user_model()
        fields = ['email', 'username', 'password']

    def create(self, validated_data):
        user_password = validated_data.get('password', None)
        db_instance = self.Meta.model(email=validated_data.get('email'), username= validated_data.get('username'))
        db_instance.set_password(user_password)
        db_instance.save()
        return db_instance
    
class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length = 200, read_only=True)
    email = serializers.CharField(max_length = 200)
    password = serializers.CharField(max_length = 200, min_length=10, style={'input_type': 'password'})
    token = serializers.CharField(max_length=255, read_only=True)

