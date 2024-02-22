"""ToDo URL Configuration."""
from django.urls import path

from todo.views import LoginView

app_name = "todo"
urlpatterns = [
    path('<int:todo_id>/', LoginView.as_view(), name="details"),
]
