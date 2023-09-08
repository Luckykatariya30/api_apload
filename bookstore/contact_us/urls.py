from django.urls import path
from .views import Userlistcreate,RetrieveUpdateDestroyAPIView

urlpatterns = [
    path('user/',Userlistcreate.as_view()),
    path('user/<int:pk>/', RetrieveUpdateDestroyAPIView.as_view()),
]