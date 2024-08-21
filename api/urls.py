from django.urls import path
from .views import CategoryList,CategoryDetail,ProductList,ProductDetail,BannerListView,BannerCreateView,BannerRedirectView
from .views import CartListView,CartCreateView,CartRedirectView,CartProductListView,CartProductCreateView,CartProductRedirectView
from .views import OrderListView,OrderCreateView,OrderRedirectView,ProductEnterListView,ProductEnterCreateView,ProductEnterRedirectView
from .views import WishListView,WishListCreateView,WishListRedirectView,InfoListView,InfoCreateView,InfoDetailView,InfoRedirectView
urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:id>/', CategoryDetail.as_view(), name='category-detail'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:id>/', ProductDetail.as_view(), name='product-detail'),
    path('', ProductList.as_view(), name='product-list'),
    path('banners/', BannerListView.as_view()),
    path('banners/<int:id>/',BannerCreateView.as_view(), name='banner-create'),
    path('banners/<int:id>/redirect/', BannerRedirectView.as_view(), name='banner-redirect'),
    path('carts/', CartListView.as_view(), name='cart'),
    path('carts/<int:id>/', CartCreateView.as_view(), name='cart-create'),
    path('carts/<int:id>/redirect/', CartRedirectView.as_view(), name='cart-redirect'),
    path('cartproducts/', CartProductListView.as_view(), name='cart-products'),
    path('cartproducts/<int:id>/',CartProductCreateView.as_view(), name='cartproduct-create'),
    path('cartproducts/<int:',CartProductRedirectView.as_view(), name='cart-product-redirect'),
    path('orders/', OrderListView.as_view(), name='order'),
    path('orders/<int:id>/', OrderCreateView.as_view(), name='order-create'),
    path('orders/<int:id/', OrderRedirectView.as_view(), name='order-redirect'),
    path('ProductEnter/', ProductEnterListView.as_view(), name='product-enter'),
    path('ProductEnter/<int:id>/', ProductEnterCreateView.as_view(), name='product'),
    path('ProductEnter/<int:id>', ProductEnterRedirectView.as_view(), name='product-enter-redirect'),
    path('wishlist/',WishListView.as_view(), name='wishlist'),
    path('wishlist/<int:id>/', WishListCreateView.as_view(), name='wishlist-create'),
    path('wishlist/<int:id>/', WishListRedirectView.as_view(), name='wishlist-redirect'),
    path('info/',InfoListView.as_view(), name='info'),
    path('info/<int:id>/', InfoCreateView.as_view(), name='info-create'),
    path('info/<int:id>/',InfoDetailView.as_view(), name='info'),
    path('info/<int:id>',InfoRedirectView.as_view(), name='info-redirect'),
    path('log-in/',views.login),

]
