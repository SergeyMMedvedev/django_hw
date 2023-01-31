from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from measurement.models import Sensor, Measurement


class SensorsListCreate(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasureListCreate(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
