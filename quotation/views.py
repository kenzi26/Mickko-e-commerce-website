from rest_framework import viewsets
from user.models import User
from .serializers import Quotation, QuotationSerializer
from rest_framework.filters import SearchFilter
from rest_framework import mixins

class QuotationViewSet(mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin,mixins.RetrieveModelMixin,  mixins.CreateModelMixin, viewsets.GenericViewSet):
    """ This allows to perform CRUD operations on all quotations in the Quotation model. 
    using the Quotation serializer and a Form parser for easy data input"""

    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer
    filter_backends = [SearchFilter]
    search_fields = ['user__id']
    

       
    