from django.urls import path
from registre import views

urlpatterns = [
    path('registre/', views.Registreapi.as_view()),
   path('registre/<int:pk>/', views.StudentDetail.as_view()),
]

