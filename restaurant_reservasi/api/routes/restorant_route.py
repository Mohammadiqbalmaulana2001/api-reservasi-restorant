from django.urls import path
from api.views.restorant_view import RestorantDetail, RestorantList

urlpatterns = [
    path('', RestorantList.as_view(), name='daftar-restorant'),
    path('<int:pk>/', RestorantDetail.as_view(), name='detail-restorant'),
]
