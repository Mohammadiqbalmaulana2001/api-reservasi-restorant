from django.urls import path
from api.views.ulasan_view import UlasanList, UlasanDetail

urlpatterns = [
  path('', UlasanList.as_view(), name="ulasan-list"),
  path("<str:pk>/", UlasanDetail.as_view(), name="ulasan-detail"),
]