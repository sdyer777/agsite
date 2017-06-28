from django.contrib import admin

from .models import WaitTime

class WaitTimeAdmin(admin.ModelAdmin):
    fields = ['visit_date', 'patient_type', 'wait_time']
    list_display = ('visit_date', 'patient_type', 'wait_time')
    list_filter = ['visit_date']



admin.site.register(WaitTime, WaitTimeAdmin)
