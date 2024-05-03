from django.urls import path,include


urlpatterns = [
  path('meja/', include('api.routes.meja_route')),
  path('restorant/', include('api.routes.restorant_route')),
  path('menu/', include('api.routes.menu_route')),
  path('pengguna/', include('api.routes.pengguna_route')),
  path('reservasi/', include('api.routes.reservasi_route')),
]