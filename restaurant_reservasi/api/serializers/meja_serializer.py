from rest_framework import serializers
from api.models import Meja

class MejaSerializer(serializers.ModelSerializer):
    restorant_url = serializers.HyperlinkedRelatedField(view_name='restorant-detail', read_only=True)
    class Meta:
        model = Meja
        fields = ['id', 'restorant', 'no_meja', 'kapasitas', 'tersewa','restorant_url']