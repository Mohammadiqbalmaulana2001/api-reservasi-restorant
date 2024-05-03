from rest_framework import serializers
from api.models import Reservasi
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image
import base64
import os

class ReservasiSerializer(serializers.ModelSerializer):
  qr_code = serializers.SerializerMethodField()
  transaksi = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='detail-transaksi-pembayaran')
  class Meta:
    model = Reservasi
    fields = ['id', 'pengguna', 'restorant','meja', 'tanggal_reservasi', 'waktu_reservasi','jumlah_orang', 'status', 'qr_code', 'transaksi']

  def get_qr_code(self, obj):
      data = f"Pengguna: {obj.pengguna}, Restoran: {obj.restorant},meja: {obj.meja}, Tanggal: {obj.tanggal_reservasi}, Waktu: {obj.waktu_reservasi}, Jumlah Orang: {obj.jumlah_orang}, Status: {obj.status}"
      qr = qrcode.make(data)

      # filename = f'reservasi_{obj.id}_qr.png'
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