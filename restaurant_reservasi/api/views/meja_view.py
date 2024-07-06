from rest_framework import generics
from api.serializers.meja_serializer import MejaSerializer
from rest_framework import mixins
from api.models import Meja
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions

class MejaList(mixins.ListModelMixin,
              mixins.CreateModelMixin,
              generics.GenericAPIView):

    queryset = Meja.objects.all()
    serializer_class = MejaSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tersewa']

    def get_queryset(self):
        return Meja.objects.all()

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

    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)