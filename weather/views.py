from django.core.cache import cache
from django.core.files.storage import default_storage
from django.core.validators import ValidationError, validate_email
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import pagination, status
from rest_framework.response import Response
from rest_framework.views import APIView

from weather.tasks import send_weather_mail
from weather.weather_data import fetch_weather_data, write_to_excel
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class EmailWeatherDataView(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        email_list = request.data.get('email_list')
        try:
            for email in email_list:
                validate_email(email)

            weather_data = cache.get('weather_data')
            if not weather_data:
                weather_data = fetch_weather_data()
                # storing in inmemory cache for 30 minutes
                cache.set('weather_data', weather_data, 30)
            
            output_path = write_to_excel(weather_data)
            # send email through celery
            send_weather_mail.delay(output_path, email_list)
            
            data = {
                'messaage' : "Mail with latest weather data send successfully"
            }
            status_code = status.HTTP_200_OK
        except  ValidationError as error:
            data = {
                "message" : "Not a valid  email id " + email 
            }
            status_code = status.HTTP_400_BAD_REQUEST
        
        
        return Response(data=data, status=status_code)


class WeatherDataView(APIView):

    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        limit = int(request.query_params.get('limit', 10))
        offset  = int(request.query_params.get('offset', 0))
        weather_data = cache.get('weather_data')
        if not weather_data:
            weather_data = fetch_weather_data()
            cache.set('weather_data', weather_data, 60)
        data = weather_data[offset:offset+limit]
        return Response(data=data)
        