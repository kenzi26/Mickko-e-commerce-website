from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import viewsets, pagination
from product.tag.models import ProductTag
from product.tag.serializers import ProductTagSerializer

class CustomPageNumberPagination(pagination.PageNumberPagination):
    page_size = 200
    page_size_query_param = 'page_size'
    max_page_size = 200

class ProductTagsViewSet(viewsets.ModelViewSet):
    '''This class is used to perform CRUD operations on the Product Tag model'''

    queryset = ProductTag.objects.filter(is_deleted=False)
    serializer_class = ProductTagSerializer
    parser_classes = [FormParser, MultiPartParser]
    pagination_class = CustomPageNumberPagination
    
