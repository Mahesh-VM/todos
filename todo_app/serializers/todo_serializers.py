from rest_framework.serializers import ModelSerializer
from todo_app.models import TodoTasks


class TodoSerializer(ModelSerializer):
    class Meta:
        """Model and fields used to serialize."""

        model = TodoTasks
        fields = [
            "task_id",
            "title",
            "description",
            "created_at",
            "updated_at",
        ]
