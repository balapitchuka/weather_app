import os
from io import BytesIO, StringIO

import requests
from django.conf import settings
from django.http import HttpResponse
from xlsxwriter.workbook import Workbook


def fetch_weather_data():
    url = 'http://api.openweathermap.org/data/2.5/find?lat=12.9&lon=76.9&cnt=30&appid=7d2e20c9e8b5b8d7c5662cd69e386248'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()['list']
    else:
        data = None 
    return data


def write_to_excel(weather_data):
    headers = ['name', 'temp_min', 'temp_max']

    excel_wb = Workbook(os.path.join(settings.STATIC_ROOT, 'weather.xlsx'))
    sheet = excel_wb.add_worksheet('data')
    
    for index, header in enumerate(headers):
        sheet.write(0, index, header)
        
    row = 1
    col = 0
    for data in weather_data:
        col = 0
        sheet.write(row, col, data['name'])
        col += 1
        sheet.write(row, col, data['main']['temp_min'])
        col += 1
        sheet.write(row, col, data['main']['temp_max'])

        row += 1
    excel_wb.close()    
    return os.path.join(settings.STATIC_ROOT, 'weather.xlsx')



    

