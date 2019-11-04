from rest_framework import serializers
from .models import Category,Goods


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"