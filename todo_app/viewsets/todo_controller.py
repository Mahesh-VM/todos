from rest_framework.viewsets import ModelViewSet
from todo_app.models import TodoTasks
from todo_app.serializers import TodoSerializer


class TodoController(ModelViewSet):
    queryset = TodoTasks.objects.all()
    serializer_class = TodoSerializer
    http_method_names = [
        "get",
        "post",
        "put",
        "delete"
    ]
    lookup_field = 'task_id'
