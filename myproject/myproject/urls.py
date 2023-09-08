
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('registre.urls')),
    path('', include('curd_api.urls')),
]
