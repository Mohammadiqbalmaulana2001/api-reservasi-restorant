from django.urls import path
from . import views

urlpatterns = [
  path('restorant/', views.RestorantCreate.as_view(), name='restorant-create')
]