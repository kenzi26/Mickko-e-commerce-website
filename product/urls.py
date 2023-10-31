from rest_framework import routers
from .views import ProductsViewSet, ProductCouponsViewSet, ProductCategoriesViewSet,FavouriteProductViewSet, \
     ComboProductViewSet, ProductSearchViewSet
from .tag.views import ProductTagsViewSet
    
router = routers.DefaultRouter()
#PRODUCTS ENDPOINTS
router.register(r'categories', ProductCategoriesViewSet, basename="products_categories")

#PRODUCTS ENDPOINTS
router.register(r'coupons', ProductCouponsViewSet, basename="products_coupons")
#router.register(r'stats', ProductStatsViewSet, basename='product-stats')
router.register(r'tags', ProductTagsViewSet, basename='product-tags')
router.register(r'combo', ComboProductViewSet, basename='product-combo')
router.register(r'product/search/(?P<tag>[\w\s]+)', ProductSearchViewSet, basename="product-search-by-tags")

#PRODUCT-COMBO ENDPOINTS

#Favorite-Product ENDPOINTS
router.register(r'favourite_product', FavouriteProductViewSet, basename="favourite_product")

#PRODUCTS ENDPOINTS
router.register(r'', ProductsViewSet, basename="products")



urlpatterns = router.urls
