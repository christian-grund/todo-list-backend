from rest_framework import serializers
from todolist.models import TodoItem
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token



class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = '__all__'
        # fields = ['title', 'author', 'created_at', 'checked']



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        Token.objects.create(user=user)
        return user