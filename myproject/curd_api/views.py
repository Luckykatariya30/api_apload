from .models import Student
from .serializers import SerializerStudent
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def Student_api(requests):
    if requests.method == 'GET':
        json_data = requests.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        if id != None:
            stu = Student.objects.get(id = id)
            serializer = SerializerStudent(stu)
            json = JSONRenderer().render(serializer.data)
            return HttpResponse(json , content_type = "application/json")
        stu = Student.objects.all()
        serializer = SerializerStudent(stu , many = True)
        json = JSONRenderer().render(serializer.data)
        return HttpResponse(json , content_type = "application/json")
    
    if requests.method == "POST":
        json_data = requests.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = SerializerStudent(data = python_data ,)
        if serializer.is_valid():
            serializer.save()
            mas = {"massage":"data is created"}
            json_data = JSONRenderer().render(mas)
            return HttpResponse(json_data ,content_type = "application/json")
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type = "application/json")


    if requests.method == "PUT":
        json_data = requests.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id = id)
        serializer = SerializerStudent(stu,data = python_data ,partial = True)
        if serializer.is_valid():
            serializer.save()
            mas = {"massage":"data is update"}
            json_data = JSONRenderer().render(mas)
            return HttpResponse(json_data ,content_type = "application/json")
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type = "application/json")
    
    if requests.method == 'DELETE':
        json_data = requests.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        mas = {"massage":"data is dalete"}
        json_data = JSONRenderer().render(mas)
        return HttpResponse(json_data ,content_type = "application/json")



