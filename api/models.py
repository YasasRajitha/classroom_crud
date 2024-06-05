from django.db import models
from django.conf import settings

# Create your models here.

class Task(models.Model):
    task_name = models.CharField(max_length=255,null=False)
    task_description = models.TextField(null=True,blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    current_user = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.id} : {self.task_name} by {self.current_user}"
    


class TaskStatus(models.Model):
    TASK_ONGOING = 'O'
    TASK_COMPLETED = 'C'

    STATUS_CHOICES = [
        (TASK_ONGOING,'Ongoing'),
        (TASK_COMPLETED,'Completed'),
    ]

    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    task_status = models.CharField(max_length=1,choices=STATUS_CHOICES,default=TASK_ONGOING)
