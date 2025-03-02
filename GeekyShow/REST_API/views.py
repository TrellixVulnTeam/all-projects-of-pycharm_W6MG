from django.shortcuts import render

# Create your views here.

from REST_API.models import Student
from REST_API.serialisers import StudentSerializer
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


def StudentView(request):
    student = Student.objects.get(id=2)
    # print(student)
    serializer = StudentSerializer(student)
    # print(serializer)
    json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    return HttpResponse(json_data,content_type='application/json')


def StudentViewWithId(request,pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')

def StudentListtView(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student,many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')



