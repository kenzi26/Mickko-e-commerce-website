from rest_framework import routers
from .views import UserViewSet


router = routers.DefaultRouter()

#Blog-comment Endpoint
router.register(r'',UserViewSet, basename="user")




urlpatterns = router.urls