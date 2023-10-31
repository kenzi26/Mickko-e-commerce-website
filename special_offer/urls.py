from rest_framework import routers
from .views import SpecialOfferViewSet

    
router = routers.DefaultRouter()

#contact-us
router.register(r'', SpecialOfferViewSet, basename="special_offer")


urlpatterns = router.urls