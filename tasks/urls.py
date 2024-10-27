from django.urls import path
from . import views


urlpatterns = [
    path('',views.TasksListview.as_view(),name='tasks'),
    path('tasktype',  views.TaskTypeList.as_view(), name='tasktype'),
    path('taskjob', views.TaskJobList.as_view(), name='taskjob'),
    path('showtasklist/<int:id>', views.TaskDetialview.as_view(), name='showtasklist'),
    path('showtasks/<int:id>', views.showtasks, name='showtasks'),
    path('task_create',  views.TaskCreateview.as_view(), name='task_create'),
     path('task_update/<int:pk>', views.TaskUpdateview.as_view(), name='task_update'),

  
]