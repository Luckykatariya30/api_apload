
from django.contrib import admin
from django.urls import path , include
# from contact_us import views
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()

# router.register('user',views.Userlistcreate,basename='user')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include('contact_us.urls')),
]
