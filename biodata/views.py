from rest_framework import viewsets, generics, mixins
from rest_framework.response import Response
from rest_framework import status
from .serializers import BioData, BioDataSerializer
from accounts.permissions import IsAdminOrReadOnly, IsAdmin, IsOwner, IsOwnerOrReadOnly

class BioDataViewSet(viewsets.ViewSet,
                       generics.GenericAPIView,
                       mixins.ListModelMixin):
    queryset = BioData.objects.all()
    serializer_class = BioDataSerializer
    permission_classes = [IsAdminOrReadOnly]

    
