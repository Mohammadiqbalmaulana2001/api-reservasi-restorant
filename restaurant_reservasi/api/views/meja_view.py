from rest_framework import generics
from api.serializers.meja_serializer import MejaSerializer
from rest_framework import mixins
from api.models import Meja

class MejaList(mixins.ListModelMixin,
              mixins.CreateModelMixin,
              generics.GenericAPIView):

    queryset = Meja.objects.all()
    serializer_class = MejaSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MejaDetail(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):

    queryset = Meja.objects.all()
    serializer_class = MejaSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)