from django.forms import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from Goods.models import Category , Product,Banner,ProductImg, Cart,CartProduct,Order,ProductEnter,WishList, Info


from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login
from .Serializer import CategorySerializer,ProductSerializer,BannerSerializer,CartSerializer,CartProductSerializer,CartProductSerializer,ProductEnterSerializer,WishlistSerializer,InfoSerializer,OrderSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required




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


@api_view(['POST'])
def register(request):
    serializer = serializers.UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def logout(request):
    request.user.auth_token.delete()
    return Response(status=204)



class ProductCreateView(APIView):
    def post(self, request):
        serializer = serializers.ProductDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def product_delete(request, pk):
    product = get_object_or_404(models.Product, pk=pk)
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class AddToCartView(APIView):
    @login_required
    def post(self, request, product_id):
        product = get_object_or_404(models.Product, id=product_id)
        cart, _ = models.Cart.objects.get_or_create(author=request.user, is_active=True)
        product_img = product.images.first()
        cart_product, _ = models.CartProduct.objects.get_or_create(
            productImg=product_img,
            product=product,
            cart=cart
        )
        cart_product.quantity += 1
        cart_product.total_price = cart_product.quantity * product.price
        cart_product.save()
        return Response(status=status.HTTP_200_OK)


"vazifa_4"

class BannerListView(APIView):
    banner=Banner.objects.all()
    serializer_class=BannerSerializer


class BannerCreateView(generics.CreateAPIView):
    banner = Banner.objects.all()
    serializer_class=BannerSerializer

class BannerRedirectView(generics.RetrieveUpdateDestroyAPIView):
    banner = Banner.objects.all()
    serializer_class=BannerSerializer

class CartListView(generics.ListAPIView):
    queryset=models.Cart.objects.all()
    serializer_class=CartSerializer

class CartCreateView(generics.CreateAPIView):
    queryset =models.Cart.objects.all()
    serializer_class=CartSerializer


class CartRedirectView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Cart.objects.all()
    serializer_class=CartSerializer

class CartProductListView(generics.ListAPIView):
    queryset=CartProduct.objects.all()
    serializer_class=CartProductSerializer

class CartProductCreateView(generics.CreateAPIView):
    queryset=CartProduct.objects.all()
    serializer_class=CartProductSerializer

class CartProductRedirectView(generics.RetrieveUpdateDestroyAPIView):
    queryset=CartProduct.objects.all()
    serializer_class=CartProductSerializer


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class=OrderSerializer


class OrderCreateView(generics.CreateAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer


class OrderRedirectView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer


class ProductEnterListView(generics.ListAPIView):
    queryset = ProductEnter.objects.all()
    serializer_class=ProductEnterSerializer


class ProductEnterCreateView(generics.CreateAPIView):
    queryset = ProductEnter.objects.all()
    serializer_class=ProductEnterSerializer


class ProductEnterRedirectView(generics.RetrieveUpdateDestroyAPIView):
    queryset=ProductEnter.objects.all()
    serializer_class=ProductEnterSerializer


class WishListView(generics.ListAPIView):
    queryset=WishList.objects.all()
    serializer_class=WishlistSerializer


class WishListCreateView(generics.CreateAPIView):
    queryset = WishList.objects.all()
    serializer_class=WishlistSerializer


class WishListRedirectView(generics.RetrieveUpdateDestroyAPIView):
    queryset=WishList.objects.all()
    serializer_class=WishlistSerializer


class InfoListView(APIView):
    queryset=Info.objects.all()
    serializer_class=InfoSerializer


class InfoCreateView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=InfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class InfoDetailView(APIView):
    def get(self,request,id ,*args,**kwargs):
        info=Info.objects.get(Info,id=id)
        serializer=InfoSerializer( info , many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class InfoRedirectView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Info.objects.all()
    serializer_class=InfoSerializer















