import os
import pytz

from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.template import loader
from django.db.models import Count, Avg, Func
from django.utils.dateparse import parse_datetime

from .models import WaitTime

csvfilename = ''

class Round(Func):
    function = 'ROUND'
    template='%(function)s(%(expressions)s, 1)'

def index(request):
    wait_time_list = WaitTime.objects.extra({'visit_date':"date(visit_date)"}).values('visit_date').annotate(avg_wait_time=Round(Avg('wait_time'))).annotate(visit_count=Count('visit_date', distinct=True)).order_by('visit_date')[:1000]
    template = loader.get_template('codesample/index.html')
    context = {
        'wait_time_list': wait_time_list,
        'csvfilename': csvfilename
        }
    return HttpResponse(template.render(context, request))

def uploadfile(request):
    """upload CSV file, validate it, replace data in DB
    """
    try:
        if request.method == 'POST' and request.FILES['csvfile']:
             # open file
            csvfile = request.FILES['csvfile']
            fs = FileSystemStorage()
            csvfilename = fs.save(csvfile.name, csvfile)
            uploaded_file_url = fs.url(csvfilename)
            # erase existing data
            WaitTime.objects.all().delete()
            # read CSV data into database
            f = open(csvfilename, 'r')  
            for line in f:
                line =  line.split(',')
                # localize the "naive" time from the CSV file. (avoids runtime error "received a naive dattime when time zone support is active".)
                naive = parse_datetime(line[0])
                line_visit_date = pytz.timezone("UTC").localize(naive, is_dst=None)
                # create and save WaitTime object
                tmp = WaitTime(visit_date=line_visit_date, patient_type=line[1].strip(), wait_time=line[2])
                tmp.save()
            f.close()
            # delete uploaded file
            os.remove(csvfilename)
            # redirect to index, which shows the new data
            return HttpResponseRedirect(reverse('codesample:index'))
    except:
        # if we have a file name (would be blank if exception occured before it was set), remove it
        if csvfilename:
            os.remove(csvfilename)
        # recired to index, which shows error message in this case
        return HttpResponseRedirect(reverse('codesample:index'))


def downloadsamplefile(request):
    """download sample CSV file, which user can use as a reference
    """
    with open('codesample/sampledata.csv', 'rb') as samplefile:
        response = HttpResponse(samplefile.read(), content_type="application/text")
        response['Content-Disposition'] = 'attachment; filename=sampledata.csv'
        return response
    raise Http404

