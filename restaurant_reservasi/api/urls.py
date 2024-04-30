from django.urls import path,include

urlpatterns = [
  path('restorant/', include('api.routes.restorant_route')),
]