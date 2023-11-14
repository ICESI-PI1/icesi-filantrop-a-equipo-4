import os
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from ..models import Sponsor
from ..models import Report
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse


def getInfo(request):
    sponsors = Sponsor.objects.all()
    return render(request, 'getInformation.html', {
        'sponsors': sponsors
        })


def agreement(request, sponsor_id):
    sponsors = Sponsor.objects.all()
    selected_sponsor = get_object_or_404(Sponsor, pk=sponsor_id)
    latest_report = None

    if Report.objects.filter(sponsor_id=selected_sponsor).exists(): 
        latest_report = Report.objects.filter(sponsor_id=selected_sponsor).latest('dateTimeOfUpload') 
    else: None

    if request.method == "POST" and request.FILES.get("uploadedFile"):
        uploaded_file = request.FILES["uploadedFile"]

        # Eliminar el reporte anterior del sistema de archivos
        if latest_report:
            report_path = os.path.join(settings.FILES_ROOT, str(latest_report.uploadedFile))
            os.remove(report_path)
            latest_report.delete()

        original_filename, file_extension = os.path.splitext(uploaded_file.name)

        new_filename = f"{selected_sponsor.name}-acuerdo{file_extension}"

        report = Report.objects.create(
            uploadedFile=new_filename,
            sponsor_id=selected_sponsor
        )

        report_path = os.path.join(settings.FILES_ROOT, new_filename)
        with open(report_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

    return render(request, 'agreement.html', {"sponsors": sponsors, "selected_sponsor": selected_sponsor, "file": latest_report})
    
    
def get(self, request, pdf_filename):
        pdf_path = os.path.join(settings.BASE_DIR, 'agreements_pdf', pdf_filename)

        with open(pdf_path, 'rb') as pdf_file:
            response = HttpResponse(pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'filename="{pdf_filename}"'

        return response

