from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update-completed/<int:pk>', views.update_completed, name='update_completed'),
    path('add-task/', views.add_task, name='add_task'),
    path('delete-task/<int:pk>', views.delete_task, name='delete_task'),
    path('edit-task/<int:pk>', views.edit_task, name='edit_task'),
    path('task-detail/<slug:slug>', views.task_detail, name='task_detail')
]
