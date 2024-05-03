from rest_framework import serializers
from api.models import PenggunaKhusus

class PenggunaSerializer(serializers.ModelSerializer):
  reservasi = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='detail-reservasi')
  class Meta:
    model = PenggunaKhusus
    fields = ['id', 'username', 'first_name', 'last_name','nomor_telepon', 'alamat', 'reservasi']

  