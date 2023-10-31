from rest_framework import routers
from .views import QuotationViewSet

    
router = routers.DefaultRouter()

#contact-us
router.register(r'', QuotationViewSet, basename="quotation")


urlpatterns = router.urls