from rest_framework import serializers
from api.models import Ulasan

class UlasanSerializer(serializers.ModelSerializer):
  class Meta:
    model = Ulasan
    fields = '__all__'