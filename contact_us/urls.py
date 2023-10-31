from rest_framework import routers
from .views import ContactUsViewSet

    
router = routers.DefaultRouter()

#contact-us
router.register(r'', ContactUsViewSet, basename="contact_us")


urlpatterns = router.urls