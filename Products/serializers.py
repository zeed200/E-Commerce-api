from rest_framework import serializers
from .models import Category, Product, ProductImage, Review
from django.contrib.auth import get_user_model

User = get_user_model()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['slug']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image', 'alt_text']


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  

    class Meta:
        model = Review
        fields = ['user', 'rating', 'comment', 'created_at']


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['full_name']  


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    seller = SellerSerializer()
    images = ProductImageSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'price',
            'category',
            'seller',
            'images',
            'reviews',
            'created_at',
            'updated_at',
        ]
