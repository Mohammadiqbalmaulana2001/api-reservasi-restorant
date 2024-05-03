from rest_framework import serializers
from api.models import Restorant

class RestorantSerializer(serializers.HyperlinkedModelSerializer):
  daftar_meja = serializers.HyperlinkedIdentityField(many=True , read_only=True, view_name='detail-meja')
  daftar_menu = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='menu-detail')
  reservasi = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='detail-reservasi')
  ulasan = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='ulasan-detail')
  class Meta:
    model = Restorant
    fields = ['id', 'nama', 'alamat', 'no_telp', 'waktu_buka', 'waktu_tutup' , 'daftar_meja', 'daftar_menu', 'reservasi', 'ulasan']