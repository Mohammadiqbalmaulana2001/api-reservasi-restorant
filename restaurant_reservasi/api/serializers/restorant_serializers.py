from rest_framework import serializers
from api.models import Restorant
from api.serializers.meja_serializer import MejaSerializer

class RestorantSerializer(serializers.HyperlinkedModelSerializer):
  daftar_meja = MejaSerializer(many=True , read_only=True)
  daftar_menu = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='menu-detail')
  reservasi = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='detail-reservasi')
  class Meta:
    model = Restorant
    fields = ['id', 'nama', 'alamat', 'no_telp', 'waktu_buka', 'waktu_tutup' , 'daftar_meja', 'daftar_menu', 'reservasi']