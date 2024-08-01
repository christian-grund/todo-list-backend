from django.contrib import admin
from django.urls import path
from todolist.views import LoginView, LogoutView, TodoItemsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('todos/', TodoItemsView.as_view(), name='todos'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
