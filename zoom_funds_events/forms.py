from django import forms
from .models import Event, Grant

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('title', 'date', 'num_attendees', 'description')

class GrantForm(forms.ModelForm):
    
    class Meta:
        model = Grant
        fields = ('funder', 'grant_title', 'date_applied', 'amount', 'date_funds_received', 'grant_start_date', 'grant_end_date', 'funding_requirements')