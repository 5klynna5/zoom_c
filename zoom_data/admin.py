from django.contrib import admin
from .models import Resident, Goal, Progress, Contact, Activity, Attendance, Child, ChildAttendance, Household, ExitInterview
from django.http import HttpResponse
from django.core import serializers

import csv
from django.http import HttpResponse, HttpResponseForbidden
from django.template.defaultfilters import slugify
##from django.db.models.loading import get_model
try:
    from django.apps import apps
    get_model = apps.get_model
except:
    from django.db.models.loading import get_model


def export(modeladmin, request, queryset):
    model = queryset.model
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s.csv' % slugify(model.__name__)
    writer = csv.writer(response)
    # Write headers to CSV file
    headers = []
    for field in model._meta.fields:
    	headers.append(field.name)
    writer.writerow(headers)
    # Write data to CSV file
    for obj in queryset:
        row = []
        for field in headers:
            if field in headers:
                val = getattr(obj, field)
                if callable(val):
                    val = val()
                row.append(val)
        writer.writerow(row)
    # Return CSV file to browser as download
    return response


admin.site.add_action(export, 'export_selected')

admin.site.register(Resident)
admin.site.register(Goal)
admin.site.register(Progress)
admin.site.register(Contact)
admin.site.register(Activity)
admin.site.register(Attendance)
admin.site.register(Child)
admin.site.register(ChildAttendance)
admin.site.register(Household)
admin.site.register(ExitInterview)