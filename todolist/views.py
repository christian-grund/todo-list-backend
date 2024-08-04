from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from todolist.serializers import TodoItemSerializer
from todolist.models import TodoItem
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
# from django.contrib.auth.models import User

# Classes are called like the models
class TodoItemsView(APIView):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticated] # IsAuthenticated

    def get(self, request, format=None):
        todos = TodoItem.objects.filter(author=request.user)
        serializer = TodoItemSerializer(todos, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        print("Request data:", request.data)  # Debugging-Ausgabe
        # serializer = TodoItemSerializer(data=request.data)
        # Ensure the author field is not included in the incoming data
        data = request.data.copy()  # Make a copy of the request data
        if 'author' in data:
            del data['author']  # Remove the author field if present

        serializer = TodoItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("Serializer errors:", serializer.errors)  # Debugging-Ausgabe
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

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


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        }, status=status.HTTP_201_CREATED)
    
