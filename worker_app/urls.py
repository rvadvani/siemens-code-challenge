from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/files', views.list_files, name='list_files'),
    path('api/file/<str:filename>', views.get_file, name='get_file'),
]
