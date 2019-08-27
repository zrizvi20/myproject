from django.urls import path
from . import views

##app_name: 'projects'

urlpatterns = [
    path('<int:user_id/projects', views.projects, name='projects'),
    ]
