from rest_framework import viewsets, generics, mixins
from rest_framework.response import Response
from rest_framework import status
from .serializers import Hero, HeroSerializer
from accounts.permissions import IsAdminOrReadOnly, IsAdmin, IsOwner, IsOwnerOrReadOnly


class HeroViewSet(viewsets.ViewSet,
                       generics.GenericAPIView,
                       mixins.ListModelMixin):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    permission_classes = [IsAdminOrReadOnly]


    
