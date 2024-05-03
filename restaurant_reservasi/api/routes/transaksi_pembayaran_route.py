from django.urls import path
from api.views.transaksi_pembayaran_view import TransaksiPembayaranList, TransaksiPembayaranDetail

urlpatterns = [
  path('', TransaksiPembayaranList.as_view(), name='daftar-transaksi-pembayaran'),
  path('<str:pk>/', TransaksiPembayaranDetail.as_view(), name='detail-transaksi-pembayaran'),
]