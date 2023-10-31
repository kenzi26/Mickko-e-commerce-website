
from rest_framework import viewsets
from product.brand.models import ProductBrand
from product.brand.serializers import ProductBrandSerializer
class ProductBrandsViewSet(viewsets.ViewSet):
    '''This class is used to perform CRUD operations on the Product Tag model'''

    queryset = ProductBrand.objects.all()
    serializer_class = ProductBrandSerializer