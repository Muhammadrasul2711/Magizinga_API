from django.urls import path, include
from Goods import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.main, name='index'),
    path('authentication/', include('Goods.authentication.urls')),
    path('back-office/', include('Goods.back-office.urls')),
    path('user/', include('Goods.user.urls')),
    path('api/', include('api.urls'))


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


