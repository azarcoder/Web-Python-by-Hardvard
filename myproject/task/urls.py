from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("taskss", views.tas, name="taskss"),
    path("addtask", views.add, name="addtask"),
]
