from rest_framework import routers
from .views import BlogViewSet


    
router = routers.DefaultRouter()


#Blog Endpoint
router.register(r'', BlogViewSet, basename="blog-post")


urlpatterns = router.urls