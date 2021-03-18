
from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create, name="create.newjob"), #localhost:8000/newjob/create
    path('read', views.read, name="read.newjob"), #localhost:8000/newjob/read
    path('update/<int:job_id>', views.update, name="update.newjob"), #localhost:8000/newjob/update/id
    path('delete/<int:job_id>', views.delete, name="delete.newjob"), #localhost:8000/newjob/delete/id
]