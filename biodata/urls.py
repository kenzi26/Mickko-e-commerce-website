from rest_framework import routers
from .views import BioDataViewSet

    
router = routers.DefaultRouter()

#contact-us
router.register(r'', BioDataViewSet, basename="biodata")


urlpatterns = router.urls