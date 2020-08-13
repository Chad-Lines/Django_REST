from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    '''
    This will serialize the model that we specify
    '''
    class Meta:
        model = Task
        fields = '__all__'