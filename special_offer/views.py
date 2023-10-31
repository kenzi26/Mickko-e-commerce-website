from rest_framework import viewsets
from .serializers import SpecialOffer, SpecialOfferSerializer
from accounts.permissions import IsAdminOrReadOnly, IsAdmin, IsOwner, IsOwnerOrReadOnly
from rest_framework.filters import SearchFilter


class SpecialOfferViewSet(viewsets.ModelViewSet):
    """This class is used to perform CRUD operations on the SpecialOffer model"""

    queryset = SpecialOffer.objects.all()
    serializer_class = SpecialOfferSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['user__id']
