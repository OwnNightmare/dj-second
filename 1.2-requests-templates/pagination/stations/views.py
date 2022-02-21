from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator, PageNotAnInteger
from django.shortcuts import render, redirect
from django.urls import reverse
import csv
import json


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request: WSGIRequest):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = request.GET.get('page', '1')
    if page_number.isdigit():
        page_number = int(page_number)
        with open('data-398-2018-08-30.csv', encoding='utf-8') as fdict:
            read_data = csv.DictReader(fdict)
            dic = (map(dict, read_data))
            stations_list = [row for row in dic]
        paginator = Paginator(stations_list, 20)
        page = paginator.get_page(page_number)
        context = {
            'bus_stations': page.object_list,
            'page': page,
        }
        return render(request, 'stations/index.html', context)
    else:
        raise PageNotAnInteger('Номер страницы должен быть целым числом!')
