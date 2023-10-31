from rest_framework import serializers
from .models import ProductTag


class ProductTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTag
        fields = '__all__'   
        read_only_fields = ['slug']  

 
