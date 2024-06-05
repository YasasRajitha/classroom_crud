from rest_framework import serializers
from django.conf import settings
from .models import Task,TaskStatus

# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = settings.AUTH_USER_MODEL
#         fields = ['id','username','first_name','last_name','phone','email','password','re_password']

class TaskSerializer(serializers.ModelSerializer):

    current_user = serializers.CharField(max_length=255,read_only=True)
    assigned_student = serializers.CharField(max_length=255,read_only=True)

    class Meta:
        model = Task
        fields = ['task_name','task_description','user','current_user','assigned_student']

    def create(self, validated_data):
        cur_user = self.context['cur_user']

        return Task.objects.create(current_user=cur_user,**validated_data)

class TaskStatusSerializer(serializers.ModelSerializer):

    # assigned_tasks = serializers.SerializerMethodField(method_name='task_id_n_name')

    # def task_id_n_name(self):
    #     current_user = self.request.user
    #     return Task.objects.filter(user_id=current_user)

    class Meta:
        model = TaskStatus
        fields = ['task','task_status']

