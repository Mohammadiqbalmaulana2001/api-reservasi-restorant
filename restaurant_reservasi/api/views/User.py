from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from api.serializers.User import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        Token.objects.get_or_create(user=user)
