from django.urls import path
from measurement.views import SensorsListCreate, SensorRetrieveUpdate, MeasureListCreate


urlpatterns = [
    path('sensors/', SensorsListCreate.as_view(), name='sensors'),
    path('sensors/<pk>/', SensorRetrieveUpdate.as_view(), name='sensors'),
    path('measurements/', MeasureListCreate.as_view(), name='measurements'),
]
