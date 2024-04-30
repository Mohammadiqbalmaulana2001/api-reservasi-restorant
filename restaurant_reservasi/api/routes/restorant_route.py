from django.urls import path
from api.views.restorant_view import RestorantDetail, RestorantList

urlpatterns = [
    path('', RestorantList.as_view(), name='restorant-list'),
    path('<int:pk>/', RestorantDetail.as_view(), name='restorant-detail'),
]
