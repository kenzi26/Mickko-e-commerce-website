from rest_framework import routers
from .views import QuotationItemViewSet

    
router = routers.DefaultRouter()

#contact-us
router.register(r'', QuotationItemViewSet, basename="quotation-items")


urlpatterns = router.urls