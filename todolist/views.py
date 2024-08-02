from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from todolist.serializers import TodoItemSerializer, UserSerializer
from todolist.models import TodoItem
# from django.contrib.auth.models import User

# Classes are called like the models
class TodoItemsView(APIView):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticated] # IsAuthenticated

    def get(self, request, format=None):
        todos = TodoItem.objects.filter(author=request.user)
        serializer = TodoItemSerializer(todos, many=True)
        return Response(serializer.data)
    

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        try:
            # Delete the token to force a login
            request.user.auth_token.delete()
            return Response(status=status.HTTP_200_OK)
        except AttributeError:
            # Handle case where token doesn't exist (e.g., already logged out)
            return Response({"error": "No token found or already logged out"}, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer

    
