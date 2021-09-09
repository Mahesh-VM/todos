from django.db import models


class TodoTasks(models.Model):
    task_id = models.BigAutoField(primary_key=True, db_index=True)
    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'todo].[todo_task'
