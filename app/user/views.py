from rest_framework import generics

from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user user"""
    serializer_class = UserSerializer
