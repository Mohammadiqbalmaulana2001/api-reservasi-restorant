from django.urls import path
from api.views.meja_view import MejaList ,MejaDetail

urlpatterns = [
  path('', MejaList.as_view(), name='daftar-meja'),
  path('<int:pk>/', MejaDetail.as_view(), name='detail-meja'),
]