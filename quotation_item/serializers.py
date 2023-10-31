from rest_framework import serializers
from .models import QuotationItem


class QuotationItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuotationItem
        fields = ('product', 'quantity', 'product_name')
