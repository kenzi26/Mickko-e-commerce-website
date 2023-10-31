from rest_framework import serializers
from .models import Quotation
from quotation_item.serializers import QuotationItemSerializer
from .controllers import QuotationController

class QuotationSerializer(serializers.ModelSerializer):
    quotation_items = QuotationItemSerializer(many=True)
    class Meta:
        model = Quotation
        fields = ('id', 'name', 'email', 'phone', 'quotation_items', 'message', 'user', 'status', 'date', 'product_images', 'product_name')

    def create(self, validated_data):
        quotation_items =validated_data.pop('quotation_items')
        instance = Quotation.objects.create(**validated_data)
        for quotation_item in quotation_items:
            instance.quotation_items.create(**quotation_item)
        QuotationController.send_create_quote_mail(instance)
        return instance

    def to_representation(self, instance):
        representation = super(QuotationSerializer, self).to_representation(instance)
        return representation 

