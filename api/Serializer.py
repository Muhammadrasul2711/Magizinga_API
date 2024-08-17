from rest_framework import serializers
from Goods.models import Category , Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        modeel=Category
        fields='__all__'

class ProductSerializer(serializers.ModelSerializer):
    prodoct=CategorySerializer(many=True,read_only=True)
    class Meta:
        model=Product
        fields='__all__'











