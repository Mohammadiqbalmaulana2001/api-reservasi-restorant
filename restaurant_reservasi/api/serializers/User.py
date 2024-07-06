from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    reservasi = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='detail-reservasi')
    ulasan = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='ulasan-detail')
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'token', 'reservasi', 'ulasan']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        token, created = Token.objects.get_or_create(user=user)
        return user

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance

    def get_token(self, obj):
        token, created = Token.objects.get_or_create(user=obj)
        return token.key
