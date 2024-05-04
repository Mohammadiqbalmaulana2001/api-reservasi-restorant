from rest_framework import mixins
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from api.models import PenggunaKhusus
from api.serializers.pengguna_serializer import PenggunaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class PenggunaList(mixins.ListModelMixin, generics.GenericAPIView):
  queryset = PenggunaKhusus.objects.all()
  serializer_class = PenggunaSerializer
  filter_backends = [DjangoFilterBackend, SearchFilter]
  filterset_fields = ['username', 'nomor_telepon', 'alamat']
  search_fields = ['username', 'nomor_telepon', 'alamat']

  def get_queryset(self):
    return PenggunaKhusus.objects.all()

  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    if serializer.is_valid():
        if PenggunaKhusus.objects.filter(username=serializer.validated_data['username']).exists():
                return Response({"error": "Nama pengguna sudah digunakan."}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class PenggunaDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
  queryset = PenggunaKhusus.objects.all()
  serializer_class = PenggunaSerializer

  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)

  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)