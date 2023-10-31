from . serializers import ContactUs, ContactUsSerializer
from rest_framework.response import Response
from rest_framework import viewsets, generics, status, pagination
from drf_yasg.utils import swagger_auto_schema
from .controller import ContactUsController

class CustomPagination(pagination.PageNumberPagination):
    page_size = 200
    page_size_query_param = 'page_size'
    max_page_size = 200
    
class ContactUsViewSet(viewsets.ViewSet):
    queryset = ContactUs.objects.filter(is_deleted=False)
    serializer_class = ContactUsSerializer
    
    @swagger_auto_schema(
        request_body=ContactUsSerializer,
        responses={status.HTTP_201_CREATED: ContactUsSerializer}
    )
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            ContactUsController.send_contact_us_mail_user(instance)
            ContactUsController.send_contact_us_mail_admin(instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        queryset = self.queryset
        paginator = CustomPagination()
        page = paginator.paginate_queryset(queryset, request)
        serializer = self.serializer_class(page, many=True)
        return paginator.get_paginated_response(serializer.data)
    # def list(self, request):
    #     queryset = self.queryset
    #     serializer = self.serializer_class(queryset, many=True)
    #     return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        contact_us_instance = generics.get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(contact_us_instance)
        return Response(serializer.data)
    
    def destroy(self, request, pk=None):  # Rename 'delete' to 'destroy'
        contact_us_instance = generics.get_object_or_404(self.queryset, pk=pk)
        contact_us_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
