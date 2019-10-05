from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'company', CompanyViewSet)

api_urls = [
    path('', include(router.urls)),
]

web_urls = [
    path('', index, name='index'),
]

urlpatterns = [
    path('api/main/', include(api_urls)),
    path('', include(web_urls)),
]