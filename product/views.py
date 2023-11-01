from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, mixins, filters, response, status
from .models import Product
from .serializers import ProductSerializer, FavouriteProductSerializer
from .category.views import ProductCategoriesViewSet
from .category.models import ProductCategory
from .tag.views import  ProductTagsViewSet
from .brand.views import  ProductBrandsViewSet
from .coupon.views import  ProductCouponsViewSet
from .serializers import ProductCountSerializer
#from order.models import Order
from django.db.models import Sum
from django.utils import timezone
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination 
from rest_framework.parsers import FormParser, MultiPartParser


# class CustomPageNumberPagination(PageNumberPagination):
#     page_size = 200
#     page_size_query_param = 'page_size'
#     max_page_size = 200

class ProductsViewSet(viewsets.ModelViewSet):
    '''This class is used to perform CRUD operations on the Product model'''
    queryset = Product.objects.filter(is_deleted=False)
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('tags__name','id','name','price','category__name')
   # pagination_class = CustomPageNumberPagination  
    #permission_classes = [IsAdminOrReadOnly]
    #parser_classes = [FormParser, MultiPartParser]

# class ProductStatsViewSet(viewsets.ViewSet):
#     def list(self, request):
#         total_products = Product.objects.count()

#         # Calculate total products sold
#         total_products_sold = Order.objects.filter(status=Order.Status.completed).aggregate(total_sold=Sum('quantity'))['total_sold'] or 0

#         # Calculate total revenue ever generated
#         total_revenue = Order.objects.filter(status=Order.Status.completed).aggregate(total_revenue=Sum('_total_amount'))['total_revenue'] or 0

#         # Calculate total sales and revenue for the current day
#         current_day = timezone.now().date()
#         current_day_sales = Order.objects.filter(status=Order.Status.completed, order_date__date=current_day).aggregate(total_sold=Sum('quantity'))['total_sold'] or 0
#         current_day_revenue = Order.objects.filter(status=Order.Status.completed, order_date__date=current_day).aggregate(total_revenue=Sum('_total_amount'))['total_revenue'] or 0

#         response_data = {
#             "total_products": total_products,
#             "total_products_sold": total_products_sold,
#             "total_revenue": total_revenue,
#             "current_day_products_sold": current_day_sales,
#             "current_day_revenue": current_day_revenue,
#         }

#         return response.Response(response_data)



class FavouriteProductViewSet(viewsets.ViewSet,
                       generics.GenericAPIView,
                       mixins.RetrieveModelMixin,
                       mixins.ListModelMixin):
    serializer_class = FavouriteProductSerializer
#    pagination_class = CustomPageNumberPagination
    def get_queryset(self):
        queryset = Product.objects.filter(is_deleted=False, is_favourite=True)
        return queryset  



class ComboProductViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(is_deleted=False, tags__name="combo")
        return queryset
    
class ProductSearchViewSet(generics.GenericAPIView, viewsets.ViewSet):
    serializer_class = ProductSerializer
    # permission_classes = [IsAdminOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ["slug"]
#    pagination_class = CustomPageNumberPagination  

    def get_queryset(self):
        tag = self.kwargs.get("tag")
        queryset = Product.objects.filter(is_deleted=False, tags__name=tag)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)  
        serializer = self.get_serializer(page, many=True) 
        return self.get_paginated_response(serializer.data) 

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        try:
            obj = get_object_or_404(queryset, pk=pk)
        except:
            obj = get_object_or_404(queryset, slug=pk)
        serializer = self.serializer_class(obj)
        return response.Response(serializer.data)
