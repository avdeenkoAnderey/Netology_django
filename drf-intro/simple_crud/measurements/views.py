from rest_framework import viewsets
from .models import Sensor, Measurement
from .serializers import SensorListSerializer, SensorDetailSerializer, MeasurementSerializer


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()

    def get_serializer_class(self):
        # Для списка — краткая версия, для detail — полная
        if self.action == "retrieve":
            return SensorDetailSerializer
        return SensorListSerializer


class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

