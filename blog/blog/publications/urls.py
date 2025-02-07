from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_publication, name='add_publication'),
    path('me/', views.my_publications, name='me'),
    path('delete/<int:pk>', views.delete_publication, name='delete'),
    path('edit/<int:pk>', views.update_publication, name='edit'),
    path('add-comment/<int:pk>', views.add_comment, name='comment')
]
