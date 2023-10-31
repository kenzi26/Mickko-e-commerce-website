from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import viewsets, generics, filters, pagination, response, status
from product.category.models import ProductCategory
from product.category.serializers import ProductCategorySerializer
#from product.permissions import IsAdminOrReadOnly
from rest_framework.response import Response

class CustomPageNumberPagination(pagination.PageNumberPagination):
    page_size = 200
    page_size_query_param = 'page_size'
    max_page_size = 200

class ProductCategoriesViewSet(viewsets.ModelViewSet):
    '''This class is used to perform CRUD operations on the Product Category model'''

    queryset = ProductCategory.objects.filter(is_deleted=False)
    serializer_class = ProductCategorySerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)    
    parser_classes = [FormParser, MultiPartParser]


