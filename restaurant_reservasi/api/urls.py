from django.urls import path,include


urlpatterns = [
  path('meja/', include('api.routes.meja_route')),
  path('restorant/', include('api.routes.restorant_route')),
  path('menu/', include('api.routes.menu_route')),
]