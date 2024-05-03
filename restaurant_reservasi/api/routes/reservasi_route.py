from django.urls import path
from api.views.reservasi_view import ReservasiList, ReservasiDetail

urlpatterns = [
  path('', ReservasiList.as_view(), name='daftar-reservasi'),
  path('<str:pk>/', ReservasiDetail.as_view(), name='detail-reservasi'),
]