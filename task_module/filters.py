from django_filters.rest_framework import FilterSet
from .models import Task


class TaskFilter(FilterSet):
  class Meta:
    model = Task
    fields = {
      'task_group': ['exact'],
    }