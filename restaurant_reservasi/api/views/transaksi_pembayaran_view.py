from rest_framework import mixins
from rest_framework import generics
from api.models import TransaksiPembayaran
from api.serializers.transaksi_pembayaran_serializer import TransaksiPembayaranSerializer

class TransaksiPembayaranList(mixins.ListModelMixin,
        mixins.CreateModelMixin,
        generics.GenericAPIView):

  queryset = TransaksiPembayaran.objects.all()
  serializer_class = TransaksiPembayaranSerializer

  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)
  
class TransaksiPembayaranDetail(mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        generics.GenericAPIView):

  queryset = TransaksiPembayaran.objects.all()
  serializer_class = TransaksiPembayaranSerializer

  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)

  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)