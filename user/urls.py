from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'v1', UserViewSet)

api_urls = [
    path('', include(router.urls)),
]

web_urls = [
    path('profile', profile, name='profile'),
]

urlpatterns = [
    path('api/user/', include(api_urls)),
    path('user/', include(web_urls)),
]