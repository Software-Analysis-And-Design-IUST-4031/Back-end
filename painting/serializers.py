from rest_framework import serializers
from .models import Painting, Transaction
from .models import Like
from registering.models import CustomUser



class PaintingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Painting
        fields = ['painting_id', 'title', 'description','image', 'creation_date', 'artist' , 'price', 'material' , 'style' , 'year' , 'vertical_depth' , 'horizontal_depth']
        read_only_fields = ['artist', 'creation_date'] 

class PaintingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Painting
        fields = ['painting_id', 'title', 'description' ,'image' , 'creation_date' , 'price','material' , 'style' , 'year' , 'vertical_depth' , 'horizontal_depth']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['user', 'painting', 'created_at']


class UserLikesSumSerializer(serializers.ModelSerializer):
    total_likes = serializers.IntegerField()  
    class Meta:
        model = CustomUser
        fields = ['user_id', 'username', 'profile_picture', 'total_likes']



class PaintingDetailSerializer2(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()

    class Meta:
        model = Painting
        fields = ['painting_id', 'title', 'description', 'image', 'creation_date', 'artist', 'price', 'material', 'style', 'year', 'vertical_depth', 'horizontal_depth', 'username', 'author']
        read_only_fields = ['artist', 'creation_date']

    def get_username(self, obj):
        return obj.artist.username

    def get_author(self, obj):
        return f"{obj.artist.firstname} {obj.artist.lastname}"
    

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'user', 'amount', 'transaction_type', 'painting', 'created_at']