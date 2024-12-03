from rest_framework_nested import routers
from . import views


task_router = routers.DefaultRouter()
task_router.register('tasks', views.TaskViewSets, basename='tasks')


urlpatterns = task_router.urls
