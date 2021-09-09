from django.urls import include, path, re_path
from todo_app.viewsets import TodoController


urlpatterns = [
    re_path(r'^getall/$', TodoController.as_view({'get': 'list'}), name='todo_list'),
    re_path(r'^get/(?P<task_id>[0-9]+)/$', TodoController.as_view({'get': 'retrieve'}), name='todo_detail'),
    re_path(r'^create/$', TodoController.as_view({'post': 'create'}), name='todo_create'),
    re_path(r'^put/(?P<task_id>[0-9]+)/$', TodoController.as_view({'put': 'update'}), name='todo_update'),
    re_path(r'^delete/(?P<task_id>[0-9]+)/$', TodoController.as_view({'delete': 'destroy'}), name='todo_delete'),
]
