from rest_framework import serializers
from .models import Order
#

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
         #avoid using '__all__' here because 2 fields (product_name and product_image) were created with @property decorators and they will not be visible in the api call. 
        fields = ('id', 'special_offers', 'user', 'date_ordered', 'status', 'product_name', 'product_image')

