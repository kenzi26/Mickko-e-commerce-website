from rest_framework import generics, viewsets, mixins, pagination
from .serializers import TestimonialSerializer, Testimonial

# Create your views here.


class TestimonialViewSet(viewsets.ViewSet,
                       generics.GenericAPIView,
                       mixins.RetrieveModelMixin,
                       mixins.ListModelMixin):
    
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer