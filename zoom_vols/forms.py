from django import forms

from .models import Hours, Volunteer, VolunteerGroup

class HoursForm(forms.ModelForm):

    class Meta:
        model = Hours
        fields = ('volunteer', 'volunteer_activity', 'date', 'hours_num')
        labels = { 
        'hours_num': 'Number of hours',
        }

class VolunteerForm(forms.ModelForm):
    
    class Meta:
        model = Volunteer
        exclude = ['volunteer_id', 'date_updated']

class GroupHoursForm(forms.ModelForm):

    class Meta:
        model = VolunteerGroup
        fields = ('group_org', 'num_volunteers', 'volunteer_activity', 'date', 'hours_num')
        labels = {
        "group_org": "Group Organization",
        "num_volunteers": 'Number of volunteers',
        'hours_num': 'Number of hours',
        }