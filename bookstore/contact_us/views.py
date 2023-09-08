from .models import User
from .serializer import UserSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

class Userlistcreate(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class UserRUD(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer