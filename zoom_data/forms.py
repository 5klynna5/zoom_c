from django import forms
from .models import Resident, Goal, Progress, Household, Child, Contact, Activity, ActivitySurvey, Attendance, ChildAttendance, ExitInterview, FollowUp
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin.widgets import AdminDateWidget 
from functools import partial
from datetime import datetime
DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class GoalForm(forms.ModelForm):

    class Meta:
        model = Goal
        exclude = ('goal_resident',)

class ProgressForm(forms.ModelForm):

    class Meta:
        model = Progress
        exclude = ('goal',)

class HouseholdForm(forms.ModelForm):

    class Meta:
        model = Household
        exclude = ('id',)

class ResidentForm(forms.ModelForm):

	class Meta:
		model = Resident
		exclude = ('resident_exit', 'household')

class ChildForm(forms.ModelForm):

	class Meta:
		model = Child
		exclude = ('household',)

class PermissionsForm(forms.ModelForm):

	class Meta:
		model = Contact
		exclude = ('contact_resident','date_updated')

class ActivityForm(forms.ModelForm):

	class Meta:
		model = Activity
		exclude = ('members','children')

class AttendanceForm(forms.ModelForm):

	class Meta:
		model = Attendance
		exclude = ('activity',)

class ChildAttendanceForm(forms.ModelForm):

	class Meta:
		model = ChildAttendance
		exclude = ('activity',)   

class ExitForm(forms.ModelForm):

	class Meta:
		model = ExitInterview
		exclude = ('household',)

class FollowUpForm(forms.ModelForm):

	class Meta:
		model = FollowUp
		exclude = ('attendance',)

class ActivitySurveyForm(forms.ModelForm):

	class Meta:
		model = ActivitySurvey
		exclude = ('activity',)
		labels = {
		"NEEDS_IMPROVE" : "I needed to improve in this skill area",
		"INTERESTING": 'I thought it would be interesting',
		'INCENTIVE': 'The incentive',
		'ADVOCATE': 'My advocate recommended it',
		'OTHER_REC': 'Someone else recommended it',
		'PEOPLE': 'I knew the other people that would be there',
		'comments' : 'What other comments or suggestions do you have about this workshop?',
		'unit_type' : 'At ZOOM I live in a'
		}