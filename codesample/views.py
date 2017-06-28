from django.http import HttpResponse
from django.template import loader

from .models import WaitTime


def index(request):
    wait_time_list = WaitTime.objects.order_by('visit_date')[:100]
    template = loader.get_template('codesample/index.html')
    context = {
        'wait_time_list': wait_time_list,
        }
    return HttpResponse(template.render(context, request))
