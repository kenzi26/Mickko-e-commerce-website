from rest_framework import serializers
from .models import ProductCoupon


class ProductCouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCoupon
        fields = '__all__'    