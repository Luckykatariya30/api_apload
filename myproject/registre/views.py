from registre.models import Registre
from registre.serializers import RegistreSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Registreapi(APIView):

    def get(self, request, format=None):
        obje = Registre.objects.all()
        serializer = RegistreSerializer(obje, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RegistreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class StudentDetail(APIView):

    def get_object(self, pk):
        try:
            return Registre.objects.get(pk=pk)
        except Registre.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = RegistreSerializer(obj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = RegistreSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        obj = self.get_object(pk)
        obj.delete()
        return Response({'mag':'data deleted'})






# Create your views here.
