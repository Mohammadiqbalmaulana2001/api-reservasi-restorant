from rest_framework import serializers
from api.models import Menu

class MenuSerializer(serializers.ModelSerializer):
  class Meta:
    model = Menu
    fields = ['id', 'restorant', 'menu', 'deskripsi', 'harga']
