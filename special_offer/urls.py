from rest_framework import routers
from .views import SpecialOfferViewSet

    
router = routers.DefaultRouter()

#special offer
router.register(r'', SpecialOfferViewSet, basename="special_offer")


urlpatterns = router.urls