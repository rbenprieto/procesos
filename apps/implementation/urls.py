from rest_framework import routers
from .views import TicketViewSet, TeamsViewSet

router = routers.DefaultRouter()
router.register(r'tickets', TicketViewSet)
router.register(r'teams', TeamsViewSet)

urlpatterns = []

urlpatterns = router.urls
