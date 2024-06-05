from django.shortcuts import render
from django.db.models import F
from rest_framework.viewsets import generics,ModelViewSet

from .models import Task,TaskStatus
from .serializers import TaskSerializer,TaskStatusSerializer
# Create your views here.

class TaskViewSet(ModelViewSet):
    # queryset = Task.objects.all()
    queryset = Task.objects.annotate(assigned_student = F('user__username')).all()
    serializer_class = TaskSerializer

    def get_serializer_context(self):
        return {'cur_user' : self.request.user}

class TaskStatusViewSet(ModelViewSet):
    queryset = TaskStatus.objects.all()
    serializer_class = TaskStatusSerializer

    # def get_queryset(self):
    #     current_userid = self.request.user
    #     objects_list = Task.objects.filter(user_id=current_userid)

    #     return TaskStatus.objects.filter(task_id=objects_list[id])
