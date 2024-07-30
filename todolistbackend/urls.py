from django.contrib import admin
from django.urls import path
from todolist.views import LoginView, TodoItemView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('todos/', TodoItemView.as_view()),
]
