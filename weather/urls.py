from django.urls import path
from weather.views import WeatherDataView, EmailWeatherDataView

urlpatterns = [
    path('', WeatherDataView.as_view(), name='weather'),
    path('email/', EmailWeatherDataView.as_view(), name='weather_email'),
    
]
