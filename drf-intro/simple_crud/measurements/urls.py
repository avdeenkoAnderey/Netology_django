from rest_framework.routers import DefaultRouter
from .views import SensorViewSet, MeasurementViewSet

router = DefaultRouter()
router.register(r"sensors", SensorViewSet, basename="sensor")
router.register(r"measurements", MeasurementViewSet, basename="measurement")

urlpatterns = router.urls