from django.db import models

class WaitTime(models.Model):
    visit_date = models.DateTimeField('Visit Date')
    patient_type = models.CharField('Patient Type', max_length=1)
    wait_time = models.IntegerField('Wait Time', default=0)
