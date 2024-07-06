from rest_framework import generics
from rest_framework import mixins, permissions
from api.models import Reservasi
from api.serializers.reservasi_serializer import ReservasiSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ReservasiList(mixins.ListModelMixin,
        mixins.CreateModelMixin,
        generics.GenericAPIView):

  queryset = Reservasi.objects.all()
  serializer_class = ReservasiSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['restorant', 'pengguna', 'meja', 'status']

  # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def get_queryset(self):
    return Reservasi.objects.all()

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

  # permission_classes = [permissions.IsAuthenticated]

  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)

  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)