from rest_framework import serializers
from todolist.models import TodoItem

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = '__all__'
        # fields = ['title', 'author', 'created_at', 'checked']