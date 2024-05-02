from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from api.models import Menu
from api.serializers.menu_serializer import MenuSerializer

class MenuList(mixins.ListModelMixin,
        mixins.CreateModelMixin,
        generics.GenericAPIView):

  queryset = Menu.objects.all()
  serializer_class = MenuSerializer

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

  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)

  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)