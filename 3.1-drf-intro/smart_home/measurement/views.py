# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, DetailedSerializer, MeasurementFullSerializer


class AllObjectsView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class OneSensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = DetailedSerializer


class CreateSensorView(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    model = Sensor
    fields = ['name', 'description']


class CreateMeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementFullSerializer
    model = Measurement
    fields = ['sensor', 'temperature']


class UpdateSensorView(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    model = Sensor
    fields = ['id', 'name', 'description']


