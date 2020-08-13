from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

from .models import Task

@api_view(['GET'])
def apiOverview(request):
    # These are the url patterns we're going to create and provide
    api_urls = {
        'List': '/task-.list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/'
    }

    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()                      # These are the tasks that exist
    serializer = TaskSerializer(tasks, many=True)   # This is the serializer defined in serializers.py
    return Response(serializer.data)                # This returns the data serialized on the above line