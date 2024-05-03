from django.urls import path
from api.views.pengguna_view import PenggunaList, PenggunaDetail

urlpatterns = [
  path('', PenggunaList.as_view(), name='daftar-pengguna'),
  path('<str:pk>/', PenggunaDetail.as_view(), name='detail-pengguna'),
]