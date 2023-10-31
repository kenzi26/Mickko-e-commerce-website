from rest_framework import routers
from .views import UserProfileViewSet


router = routers.DefaultRouter()

#Blog-comment Endpoint
router.register(r'',UserProfileViewSet, basename="userprofile")




urlpatterns = router.urls