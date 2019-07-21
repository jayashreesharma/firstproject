from rest_framework import routers
from movieapp.views import *

router =routers.SimpleRouter()
router.register(r'director', DirectorViewSet)
router.register(r'actor', ActorViewSet)
router.register(r'movie', MovieViewSet)
router.register(r'country', CountryViewSet)

urlpatterns = router.urls
