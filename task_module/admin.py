from django.contrib import admin
from .models import Task
# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
  list_display = ['name', 'task_group', 'start_date', 'end_date', 'is_complete']
  list_editable =['task_group','start_date', 'end_date', 'is_complete']
  list_filter=['task_group', 'is_complete']
  ordering = ['name', 'start_date', 'end_date']
