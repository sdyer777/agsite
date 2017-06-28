import os
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.template import loader

from .models import WaitTime

csvfilename = ''

def index(request):
    wait_time_list = WaitTime.objects.order_by('visit_date')[:100]
    template = loader.get_template('codesample/index.html')
    context = {
        'wait_time_list': wait_time_list,
        'csvfilename': csvfilename
        }
    return HttpResponse(template.render(context, request))

def uploadfile(request):
    # upload CSV file, validate it, replace data in DB
    if request.method == 'POST' and request.FILES['csvfile']:
        csvfile = request.FILES['csvfile']
        fs = FileSystemStorage()
        csvfilename = fs.save(csvfile.name, csvfile)
        uploaded_file_url = fs.url(csvfilename)
        # open file
        # validate file
        # erase data
        WaitTime.objects.all().delete()
        # read CSV data into database
        f = open(csvfilename, 'r')  
        for line in f:
            line =  line.split(',')
            print (line)
            tmp = WaitTime(visit_date=line[0], patient_type=line[1], wait_time=line[2])
 #           tmp = WaitTime.objects.create()
 #           tmp.visit_date = line[0]
 #           tmp.visit_date = 'June 22, 2017, 10 a.m.'
 #           tmp.patient_type = line[1]
 #           tmp.wait_time = line[2]
            tmp.save()
        f.close()
        # redirect to index, which shows the new data
        return HttpResponseRedirect(reverse('codesample:index'))


def downloadsamplefile(request):
    """download sample CSV file, which user can use as a reference
    """
    with open('sampledata.csv', 'rb') as samplefile:
        response = HttpResponse(samplefile.read(), content_type="application/text")
        response['Content-Disposition'] = 'attachment; filename=sampledata.csv'
        return response
    raise Http404

