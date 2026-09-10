from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("lista_tarefas/", views.lista_tarefas, name="lista_tarefas"),
    path("home/", views.home,),
]
