from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from Goods.models import Category , Product
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login
from .Serializer import CategorySerializer,ProductSerializer




class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class=CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializers=CategorySerializer

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializers=ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializers=ProductSerializer
@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password =request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        token,_=Token.objects.get_or_create(user=user)
        context={
            'susses':True,
            'username':user.username,
            'key':token.key,
        }
    else:
        context={
            'susses':'Hattolik'
        }
    return Response(context)

