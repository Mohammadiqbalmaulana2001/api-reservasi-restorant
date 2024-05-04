from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
  path('meja/', include('api.routes.meja_route')),
  path('restorant/', include('api.routes.restorant_route')),
  path('menu/', include('api.routes.menu_route')),
  path('pengguna/', include('api.routes.pengguna_route')),
  path('reservasi/', include('api.routes.reservasi_route')),
  path('ulasan/', include('api.routes.ulasan_route')),
  path('transaksi-pembayaran/', include('api.routes.transaksi_pembayaran_route')),
]
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])