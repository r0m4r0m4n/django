from django.urls import path
from .views import calculate_distance_view
# from .models import Measurement

app_name = 'measurements'

urlpatterns = [
    path('', calculate_distance_view, name='navigation_map_url'),
]