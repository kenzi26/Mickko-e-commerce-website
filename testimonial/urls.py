from rest_framework import routers
from .views import TestimonialViewSet


router = routers.DefaultRouter()

#Blog-comment Endpoint
router.register(r'',TestimonialViewSet, basename="testimonials")




urlpatterns = router.urls