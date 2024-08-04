from django.contrib import admin
from django.urls import path
from todolist.views import LoginView, LogoutView, RegisterView, TodoDetail, TodoItemPatchView, TodoItemsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('todos/', TodoItemsView.as_view(), name='todos'),
    path('todos/<int:id>/', TodoDetail.as_view(), name='todo-detail'),
    path('todos/<int:pk>/patch/', TodoItemPatchView.as_view(), name='todo-item-patch'),
    path('register/', RegisterView.as_view(), name='register'),
]
