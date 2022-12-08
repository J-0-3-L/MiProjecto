
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"), #el name es para que la ruta no sea tipeada en el buscador
    path('about/', views.about, name="about"),
    path('hello/<str:username>', views.hello, name="hello"),
    path('projects/', views.projects ,name="projects"),
    path('tasks/', views.tasks, name="tasks"),
    path('create_task/', views.create_task ,name="create_task"),
    path('create_project/',views.create_project, name="create_project")
    

]