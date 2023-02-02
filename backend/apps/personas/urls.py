from rest_framework import routers
from .api import PersonasViewSet

router = routers.DefaultRouter()

router.register('api/personas', PersonasViewSet, 'personas')

urlpatterns = router.urls