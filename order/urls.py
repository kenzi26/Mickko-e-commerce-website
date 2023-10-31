from rest_framework import routers
from .views import OrderViewSet


router = routers.DefaultRouter()

#Blog-comment Endpoint
router.register(r'',OrderViewSet, basename="testimonials")




urlpatterns = router.urls