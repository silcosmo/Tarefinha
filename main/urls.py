
from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='tasks_list'),
    path('concluida', views.tasks_ok, name='tasks_ok'),
    path('pendentes', views.tasks_nok, name='tasks_nok'),
    path('create_task', views.task_create, name='task_create')
]

