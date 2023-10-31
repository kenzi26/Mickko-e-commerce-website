
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from product.coupon.models import ProductCoupon
from product.coupon.serializers import ProductCouponSerializer
class ProductCouponsViewSet(viewsets.ViewSet,generics.GenericAPIView):
    '''This class is used to perform CRUD operations on the Product Tag model'''

    queryset = ProductCoupon.objects.all()
    serializer_class = ProductCouponSerializer

    @action(methods=['GET'], url_name='apply', detail=True )
    def apply(self, request, pk=None, *args, **kwargs):
        instance = get_object_or_404(self.get_queryset(), code=pk)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)