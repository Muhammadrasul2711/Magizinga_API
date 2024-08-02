from django.urls import path
from . import views

urlpatterns = [
    path('banner_list', views.banner_list, name='banner_list'),
    path('BannerDetail/<int:id>/', views.banner_detail, name='banner_detail'),
    path('Banner/new/', views.banner_create, name='banner_create'),
    path('Banner/<int:id>/edit/', views.banner_update, name='banner_update'),
    path('Banner/<int:id>/delete/', views.banner_delete, name='banner_delete'),
]
