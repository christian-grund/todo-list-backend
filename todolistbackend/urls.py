from django.contrib import admin
from django.urls import path
from todolist.views import LoginView, LogoutView, RegisterView, TodoItemsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('todos/', TodoItemsView.as_view(), name='todos'),
    path('register/', RegisterView.as_view(), name='register'),
]
