from rest_framework import generics, viewsets, mixins, pagination
from .serializers import TestimonialSerializer, Testimonial

# Create your views here.
class CustomPagination(pagination.PageNumberPagination):
    page_size = 200
    page_size_query_param = 'page_size'
    max_page_size = 200

class TestimonialViewSet(viewsets.ViewSet,
                       generics.GenericAPIView,
                       mixins.RetrieveModelMixin,
                       mixins.ListModelMixin):
    
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    pagination_class = CustomPagination