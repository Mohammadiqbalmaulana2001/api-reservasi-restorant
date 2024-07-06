from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics , permissions
from rest_framework import mixins
from api.models import Menu
from api.serializers.menu_serializer import MenuSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class MenuList(mixins.ListModelMixin,
        mixins.CreateModelMixin,
        generics.GenericAPIView):

  queryset = Menu.objects.all()
  serializer_class = MenuSerializer
  filter_backends = [DjangoFilterBackend, SearchFilter]
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  filterset_fields = ['restorant']
  search_fields = ['menu', 'deskripsi', 'harga']

  def get_queryset(self):
    return Menu.objects.all()

  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

class MenuDetail(mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        generics.GenericAPIView):

  queryset = Menu.objects.all()
  serializer_class = MenuSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)

  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)