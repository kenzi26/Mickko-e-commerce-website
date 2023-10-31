from rest_framework import routers
from .views import HeroViewSet


router = routers.DefaultRouter()

#Blog-comment Endpoint
router.register(r'',HeroViewSet, basename="testimonials")




urlpatterns = router.urls