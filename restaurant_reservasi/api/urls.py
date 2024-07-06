from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.User import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('meja/', include('api.routes.meja_route')),
    path('restorant/', include('api.routes.restorant_route')),
    path('menu/', include('api.routes.menu_route')),
    path('reservasi/', include('api.routes.reservasi_route')),
    path('ulasan/', include('api.routes.ulasan_route')),
    path('transaksi-pembayaran/', include('api.routes.transaksi_pembayaran_route')),
    path('', include(router.urls)),
]

# Hapus penggunaan format_suffix_patterns untuk menghindari konflik regex
# urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
