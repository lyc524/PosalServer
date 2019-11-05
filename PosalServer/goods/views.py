from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet 
from .models import Category,Goods
from .serializer import CategorySerializer,GoodsSerializer

# Create your views here.

class CategoryViewSet(ModelViewSet): 
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

    
class GoodsViewSet(ModelViewSet):
    queryset=Goods.objects.all()
    serializer_class=GoodsSerializer