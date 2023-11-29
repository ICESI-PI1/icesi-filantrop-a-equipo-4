from django.http import HttpResponse
from ..loadFiles import readExcel
from django.shortcuts import render, redirect, get_object_or_404
from ..models import Sponsor, Event, Official, Sponsor_Event, Report
from django.conf import settings
import os
from django.contrib.auth.decorators import login_required

@login_required
def loadSponsors (request):

    file_path = os.path.join(settings.FILES_EXCEL_DATA_DIR, 'SponsorData.xlsx')

    if os.path.exists(file_path):
        os.remove(file_path)
        
    new_file = request.FILES['SponsorData']

    with open(file_path, 'wb+') as destino:
        for chunk in new_file.chunks():
            destino.write(chunk)

    data = readExcel(file_path)

    for obj_data in data.values():
        obj = Sponsor(
            name=obj_data['name'],
            personType=obj_data['personType'],
            contact_number=obj_data['contact_number'],
            email=obj_data['email'],
            previousColab=obj_data['previousColab']
        )
        obj.save()

    return redirect('sponsor')

@login_required
def loadEvents (request):

    file_path = os.path.join(settings.FILES_EXCEL_DATA_DIR, 'EventData.xlsx')

    if os.path.exists(file_path):
        os.remove(file_path)
        
    new_file = request.FILES['EventData']

    with open(file_path, 'wb+') as destino:
        for chunk in new_file.chunks():
            destino.write(chunk)

    data = readExcel(file_path)

    for obj_data in data.values():
        
        obj = Event(
            name=obj_data['name'],
            event_Type=obj_data['event_type'],
            date=obj_data['date'],
            time=obj_data['time']
        )
        obj.save()

        sponsor=get_object_or_404(Sponsor,name=obj_data['sponsor_name'])

        obj2 = Sponsor_Event(
            event_name=obj,
            Sponsor_id=sponsor,
            participation=obj_data['participation']
        )
        obj2.save()

    return redirect('event')

@login_required
def loadOfficial (request):

    file_path = os.path.join(settings.FILES_EXCEL_DATA_DIR, 'OfficialData.xlsx')

    if os.path.exists(file_path):
        os.remove(file_path)
        
    new_file = request.FILES['OfficialData']

    with open(file_path, 'wb+') as destino:
        for chunk in new_file.chunks():
            destino.write(chunk)

    data = readExcel(file_path)

    for obj_data in data.values():
        obj = Official(
            name=obj_data['name'],
            email=obj_data['email'],
            username=obj_data['username'],
            password=obj_data['password']
        )
        obj.save()

    return redirect('menu')

@login_required
def loadReports (request):

    file_path = os.path.join(settings.FILES_EXCEL_DATA_DIR, 'ReportData.xlsx')

    if os.path.exists(file_path):
        os.remove(file_path)
        
    new_file = request.FILES['ReportData']

    with open(file_path, 'wb+') as destino:
        for chunk in new_file.chunks():
            destino.write(chunk)

    data = readExcel(file_path)

    for obj_data in data.values():
        obj = Report(
            ...
        )
        obj.save()

    return redirect('report')


@login_required
def download_event_data(request):
    file_path = os.path.join(settings.FILES_EXCEL_DATA_FORMAT, 'EventData.xlsx')

    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=EventData.xlsx'
            return response
    return HttpResponse("File not found", status=404)

@login_required
def download_sponsor_data(request):
    file_path = os.path.join(settings.FILES_EXCEL_DATA_FORMAT, 'SponsorData.xlsx')

    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=SponsorData.xlsx'
            return response
    return HttpResponse("File not found", status=404)

@login_required
def download_official_data(request):
    file_path = os.path.join(settings.FILES_EXCEL_DATA_FORMAT, 'OfficialData.xlsx')

    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=OfficialData.xlsx'
            return response
    return HttpResponse("File not found", status=404)

