from rest_framework import routers
from .views import UserProfileViewSet


router = routers.DefaultRouter()

#userprofile Endpoint
router.register(r'',UserProfileViewSet, basename="userprofile")




urlpatterns = router.urls