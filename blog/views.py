from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import Blog, BlogSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import FormParser, MultiPartParser


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 20

class BlogViewSet(viewsets.ModelViewSet):

    queryset = Blog.objects.filter(is_deleted=False)
    serializer_class = BlogSerializer
    pagination_class = CustomPageNumberPagination 
    parser_classes = [FormParser, MultiPartParser]

    

    