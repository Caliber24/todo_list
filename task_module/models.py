from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
# Create your models here.


class Task(models.Model):
    WORK = 'W'
    PERSONAL = 'P'
    TASK_GROUP_CHOICES=[
       (WORK,'WORK'),
       (PERSONAL, 'PERSONAL')
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    task_group = models.CharField(max_length=1, default=1, choices=TASK_GROUP_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_complete = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.name