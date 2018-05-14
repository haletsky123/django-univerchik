import os
import json
from django.conf import settings
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.template import loader
from .models import Document, Clinic, Doctor, Cell
from .forms import DocumentForm


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# def take_schedule(request):
#     if request.method == 'GET':
#         return render(request, 'schedule/schedule.html')
#     elif request.method == 'POST':
#         return render(request, 'schedule/schedule.html')


def schedule_send(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            path_to_file = str(Document.objects.order_by('uploaded_at')[0].document)
            path_to_file = os.path.join(settings.BASE_DIR, path_to_file)
            with open(path_to_file) as f:
                fullData = json.load(f)
                clinics_id_to_show = []
                for clinic_id in fullData.keys():
                    if clinic_id != 'data':
                        clinics_id_to_show.append(int(clinic_id))
                        Clinic.objects.filter(id=clinic_id).delete()
                        clinic_ = Clinic(name=fullData[clinic_id], id=int(clinic_id))
                        clinic_.save()
                        parse_cells(clinic_id)
                        #massive
                        for doc_id in fullData['data'][clinic_id].keys():
                            doc = Doctor(id=doc_id, clinic=clinic_,
                                         efio=fullData['data'][clinic_id][doc_id]['efio'], )
                            doc.save()
                            while len(fullData['data'][clinic_id][doc_id]['cells']) > 0:
                                cell = fullData['data'][clinic_id][doc_id]['cells'][0]
                                cell_ = Cell(doctor=doc, date=cell['dt'], time_start=cell['time_start'],
                                             time_end=cell['time_end'], free=cell['free'])
                                fullData['data'][clinic_id][doc_id]['cells'].pop(0)
                                cell_.save()
                        #yield massive
                #for slots in parse()
                #bulk_create
            data = {}
            for clinic_id in clinics_id_to_show:
                clinic = Clinic.objects.get(pk=clinic_id)
                data[clinic.name] = {}
                for doc in Doctor.objects.filter(clinic=clinic):
                    data[clinic.name][doc.efio] = {}
                    for cell in Cell.objects.filter(doctor=doc):
                        if cell.date not in data[clinic.name][doc.efio].keys():
                            data[clinic.name][doc.efio][cell.date] = []
                        data[clinic.name][doc.efio][cell.date].append(cell)
            context = {'data': data}
            return render(request, 'schedule/cells.html', context)
    else:
        form = DocumentForm()

        return render(request, 'schedule/schedule.html', {
            'form': form
        })
