from django.urls import path

from measurement.views import AllObjectsView, OneSensorView, CreateSensorView, CreateMeasurementView, UpdateSensorView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', AllObjectsView.as_view()),
    path('sensors/create', CreateSensorView.as_view()),
    path('sensors/update', UpdateSensorView.as_view()),
    path('measurements/create', CreateMeasurementView.as_view()),
    path('sensors/<pk>', OneSensorView.as_view()),
]
