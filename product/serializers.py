from rest_framework import serializers
from .models import Product
#from .category.serializers import ProductCategorySerializer
#from .tag.serializers import ProductTagSerializer
#from .brand.serializers import ProductBrandSerializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductCountSerializer(serializers.Serializer):
    total_count = serializers.IntegerField()

class OrderProductSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Product
        fields = (
            'id',
            'sku',
            'featured_image',
            'name'
        )

               
class FavouriteProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'is_favourite': {'read_only': True}  # To make it read-only in the filtered viewset
        }            