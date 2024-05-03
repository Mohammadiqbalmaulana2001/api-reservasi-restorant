from rest_framework import generics
from rest_framework import mixins
from api.models import Reservasi
from api.serializers.reservasi_serializer import ReservasiSerializer

class ReservasiList(mixins.ListModelMixin,
        mixins.CreateModelMixin,
        generics.GenericAPIView):

  queryset = Reservasi.objects.all()
  serializer_class = ReservasiSerializer

  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)
  
class ReservasiDetail(mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        generics.GenericAPIView):

  queryset = Reservasi.objects.all()
  serializer_class = ReservasiSerializer

  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)

  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)