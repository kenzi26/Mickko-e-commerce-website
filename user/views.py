from rest_framework import viewsets
from .serializers import User, UsersSerializer
from rest_framework.filters import SearchFilter
from django.http import JsonResponse
from rest_framework.decorators import action
from .controllers import UserController

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UsersSerializer
    