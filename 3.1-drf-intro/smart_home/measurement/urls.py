from django.urls import path

from measurement.views import AllObjectsView, GetSensorView, CreateSensorView, CreateMeasurementView, UpdateSensorView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', AllObjectsView.as_view()),
    path('sensors/create', CreateSensorView.as_view()),
    path('sensors/update/<pk>', UpdateSensorView.as_view()),
    path('measurements/create', CreateMeasurementView.as_view()),
    path('sensors/<pk>', GetSensorView.as_view()),
]
