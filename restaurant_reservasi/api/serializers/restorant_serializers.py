from rest_framework import serializers
from api.models import Restorant
from api.serializers.meja_serializer import MejaSerializer

class RestorantSerializer(serializers.ModelSerializer):
  daftar_meja = MejaSerializer(many=True , read_only=True)
  class Meta:
    model = Restorant
    fields = ['id', 'nama', 'alamat', 'no_telp', 'waktu_buka', 'waktu_tutup' , 'daftar_meja']