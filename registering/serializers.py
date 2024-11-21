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
        fields = ['user_id', 'email', 'firstname', 'lastname', 'username', 'is_active', 'is_admin','date_joined', 'nickname', 'phone_number' , 'date_of_birth' ,'region' ,'gender', 'national_id' ,'address', 'profile_picture'   ]

 


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['firstname', 'lastname', 'username', 'nickname' ,'phone_number' , 'date_of_birth' ,'region' ,'gender', 'national_id' ,'address', 'profile_picture' ]































# class UserDetailSerializer(serializers.ModelSerializer):
#     phone_number = serializers.CharField(source='profile.phone_number', read_only=True)
#     date_of_birth = serializers.DateField(source='profile.date_of_birth', read_only=True)
#     region = serializers.CharField(source='profile.region', read_only=True)
#     gender = serializers.CharField(source='profile.gender', read_only=True)
#     national_id = serializers.CharField(source='profile.national_id', read_only=True)
#     address = serializers.CharField(source='profile.address', read_only=True)
#     profile_picture = serializers.ImageField(source='profile.profile_picture', read_only=True)

#     class Meta:
#         model = CustomUser
#         fields = [
#             'id', 'email', 'first_name', 'last_name', 'username', 'is_active', 
#             'is_superuser', 'date_joined', 'phone_number', 'date_of_birth', 
#             'region', 'gender', 'national_id', 'address', 'profile_picture'
#         ]













# class UserUpdateSerializer(serializers.ModelSerializer):
#     phone_number = serializers.CharField(source='profile.phone_number', required=False)
#     date_of_birth = serializers.DateField(source='profile.date_of_birth', required=False)
#     region = serializers.CharField(source='profile.region', required=False)
#     gender = serializers.CharField(source='profile.gender', required=False)
#     national_id = serializers.CharField(source='profile.national_id', required=False)
#     address = serializers.CharField(source='profile.address', required=False)
#     profile_picture = serializers.ImageField(source='profile.profile_picture', required=False)

#     class Meta:
#         model = CustomUser
#         fields = [
#             'first_name', 'last_name', 'username', 'phone_number', 'date_of_birth', 
#             'region', 'gender', 'national_id', 'address', 'profile_picture'
#         ]
#         extra_kwargs = {
#             'first_name': {'required': True},
#             'last_name': {'required': True},
#             'username': {'required': True}
#         }

#     def update(self, instance, validated_data):
#         # به‌روزرسانی فیلدهای CustomUser
#         profile_data = validated_data.pop('profile', {})
#         for attr, value in validated_data.items():
#             setattr(instance, attr, value)
#         instance.save()

#         # به‌روزرسانی فیلدهای پروفایل
#         profile = instance.profile
#         for attr, value in profile_data.items():
#             setattr(profile, attr, value)
#         profile.save()

#         return instance

























