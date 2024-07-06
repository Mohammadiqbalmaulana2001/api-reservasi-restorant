from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from api.models import Restorant
from rest_framework.exceptions import NotFound
from api.serializers.restorant_serializers import RestorantSerializer
from rest_framework.filters import SearchFilter
from rest_framework import permissions

class RestorantList(generics.ListCreateAPIView):
  queryset = Restorant.objects.all()
  serializer_class = RestorantSerializer
  permission_classes = [permissions.IsAuthenticated]
  
  filter_backends = [SearchFilter]
  search_fields = ['nama', 'alamat', 'no_telp', 'waktu_buka', 'waktu_tutup']

class RestorantDetail(APIView):
  permission_classes = [permissions.IsAuthenticated]
  def get_object(self, pk):
    try:
      return Restorant.objects.get(pk=pk)
    except Restorant.DoesNotExist:
      raise NotFound("Restorant dengan id {} tidak ditemukan".format(pk))
  
  def get(self, request, pk, format =None):
    restorant = self.get_object(pk)
    if restorant :
      serializer = RestorantSerializer(restorant)
      return Response({
        "success": True,
        "message": "Restorant ditemukan",
        "data": serializer.data
      })
    else:
      return Response({
        "success": False,
        "message": "Restorant tidak ditemukan"
      }, status=status.HTTP_404_NOT_FOUND)
  
  def put(self, request, pk, format =None):
    restorant = self.get_object(pk)
    serializer = RestorantSerializer(restorant, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({
        "success": True,
        "message": "Restorant diperbarui",
        "data": serializer.data
      })
    return Response({
      "success": False,
      "message": "Restorant tidak dapat diperbarui",
      "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format =None):
    restorant = self.get_object(pk)
    restorant.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)