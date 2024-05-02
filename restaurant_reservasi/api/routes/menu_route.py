from django.urls import path
from api.views.menu_view import  MenuList, MenuDetail

urlpatterns = [
  path('', MenuList.as_view(), name="menu-list"),
  path("<str:pk>/", MenuDetail.as_view(), name="menu-detail"),
]