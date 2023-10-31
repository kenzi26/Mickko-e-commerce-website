from rest_framework import viewsets
from .serializers import Order, OrderSerializer
from accounts.permissions import IsAdminOrReadOnly, IsAdmin, IsOwner, IsOwnerOrReadOnly
from rest_framework.filters import SearchFilter

class OrderViewSet(viewsets.ModelViewSet):
    """ This is showcases a portfolio of successful projects for Burtech"""
    
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['user__id']