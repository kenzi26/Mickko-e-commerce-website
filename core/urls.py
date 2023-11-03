from django.contrib import admin
from django.urls import path, include, re_path

# DRF YASG Imports
from django.urls import re_path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers, permissions
from drf_yasg import openapi
from django.conf.urls.static import static
from django.conf import settings


router = routers.DefaultRouter()
urlpatterns = router.urls


schema_view = get_schema_view(
   openapi.Info(
      title="MICKKO API",
      default_version='v1',
      description="Description Of API DOCs",
      contact=openapi.Contact(email="mokwenyekene1@yahoo.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns += [
    path('', include('admin_volt.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    path('api/blog/', include('blog.urls')),
    path('api/contact_us/', include('contact_us.urls')),
    path('api/testimonial/', include('testimonial.urls')),
    path('api/products/', include('product.urls')),
    path('api/special_offer/', include('special_offer.urls')),
    path('api/hero/', include('hero.urls')),
    path('api/biodata/', include('biodata.urls')),
    path('api/quotation/', include('quotation.urls')),
    path('api/quotation_item/', include('quotation_item.urls')),
    path('api/user/', include('user.urls')),
    path('api/userprofile/', include('userprofile.urls')),
    path('api/order/', include('order.urls')),
    


    

    re_path(
        r"^api/docs/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]



  

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)