from rest_framework import serializers
from api.models import TransaksiPembayaran

class TransaksiPembayaranSerializer(serializers.ModelSerializer):
  class Meta:
    model = TransaksiPembayaran
    fields = '__all__'