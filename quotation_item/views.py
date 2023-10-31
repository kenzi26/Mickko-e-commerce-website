from rest_framework import viewsets
from .serializers import QuotationItem, QuotationItemSerializer
from accounts.permissions import IsAdminOrReadOnly, IsAdmin, IsOwner, IsOwnerOrReadOnly
from rest_framework.filters import SearchFilter

class QuotationItemViewSet(viewsets.ModelViewSet):

    
    queryset = QuotationItem.objects.all()
    serializer_class = QuotationItemSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [SearchFilter]