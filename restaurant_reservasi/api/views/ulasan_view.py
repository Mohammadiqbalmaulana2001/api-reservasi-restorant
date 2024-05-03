from rest_framework import generics
from rest_framework import mixins
from api.models import Ulasan
from api.serializers.ulasan_serializer import UlasanSerializer

class UlasanList(mixins.ListModelMixin,
        mixins.CreateModelMixin,
        generics.GenericAPIView):

  queryset = Ulasan.objects.all()
  serializer_class = UlasanSerializer

  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)
  
class UlasanDetail(mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        generics.GenericAPIView):

  queryset = Ulasan.objects.all()
  serializer_class = UlasanSerializer

  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)

  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)