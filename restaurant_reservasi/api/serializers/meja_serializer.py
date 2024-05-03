from rest_framework import serializers
from api.models import Meja
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image
import base64
import os

class MejaSerializer(serializers.ModelSerializer):
    qr_code = serializers.SerializerMethodField()
    reservasi = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='detail-reservasi')
    class Meta:
        model = Meja
        fields = ['id', 'restorant', 'no_meja', 'kapasitas', 'tersewa', 'qr_code', 'reservasi']

    def get_qr_code(self, obj):
        data = f"Restoran: {obj.restorant}, Nomor Meja: {obj.no_meja}, Kapasitas: {obj.kapasitas}"
        qr = qrcode.make(data)

        # filename = f'meja_{obj.id}_qr.png'
        # save_path = os.path.join('api', 'qr_code', filename)
        # qr.save(save_path, format='PNG')

        image_io = BytesIO()
        qr.save(image_io, format='PNG')
        image_io.seek(0)

        qr_image = Image.open(image_io)

        buffered = BytesIO()
        qr_image.save(buffered, format="PNG")
        qr_base64 = base64.b64encode(buffered.getvalue()).decode()

        return qr_base64
