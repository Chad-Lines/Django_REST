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

@api_view(['GET'])
def taskDetail(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)  # Getting data from the API
    if serializer.is_valid():                       # Making sure that the data is valid
        serializer.save()                           # If so, save
    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data) # This allows us to "get" and "post" at the same time
    if serializer.is_valid():                       
        serializer.save()                           
    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Item Deleted Successfully")