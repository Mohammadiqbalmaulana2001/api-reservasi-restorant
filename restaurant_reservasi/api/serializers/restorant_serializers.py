from rest_framework import serializers
from api.models import Restorant

class RestorantSerializer(serializers.ModelSerializer):
  class Meta:
    model = Restorant
    fields = ['id', 'nama', 'alamat', 'no_telp', 'waktu_Buka', 'Waktu_Tutup']