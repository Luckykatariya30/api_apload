from django.urls import path
from .views import Student_api


urlpatterns = [
    path('student/', Student_api),

  
]