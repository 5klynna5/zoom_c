from django.db import models
from django.db.models import Sum
from django.utils import timezone

class Volunteer(models.Model):
	volunteer_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	start_date = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
	organization = models.CharField(max_length = 30, blank=True, null=True)
	
	phone = models.CharField( max_length=10, blank=True, null=True)
	email = models.EmailField(blank=True, null=True)

	STATUS_CHOICES = {
		('Active', 'ACTIVE'),
		('Inactive', 'INACTIVE',)
	}

	status = models.CharField(max_length=8, choices=STATUS_CHOICES, blank=True, null=True)

	PERMISSION_CHOICES = {
		('Yes', 'YES'),
		('No', 'NO'),
	}
	permission_text = models.CharField(max_length=3, choices=PERMISSION_CHOICES, blank=True, null=True)
	permission_photo = models.CharField(max_length=3, choices=PERMISSION_CHOICES, blank=True, null=True)
	permission_email = models.CharField(max_length=3, choices=PERMISSION_CHOICES, blank=True, null=True)
	permission_call = models.CharField(max_length=3, choices=PERMISSION_CHOICES, blank=True, null=True)
	permission_mail = models.CharField(max_length=3, choices=PERMISSION_CHOICES, blank=True, null=True)
	permission_facebook = models.CharField(max_length=3, choices=PERMISSION_CHOICES, blank=True, null=True)

	CONTACT_CHOICES = {
		('Text', 'TEXT'),
		('Call', 'CALL'),
		('Email', 'EMAIL'),
		('Mail', 'MAIL'),
		('Facebook', 'FACEBOOK'),
		('Do Not Contact', 'DO_NOT_CONTACT'),
	}

	contact_pref = models.CharField(max_length=16, choices=CONTACT_CHOICES, blank=True, null=True)

	interests = models.TextField(blank=True, null=True)

	date_updated = models.DateTimeField(blank=True, null=True)

	@property
	def total_hours(self):
		if self.hours_set.all().order_by('-id').first() is None:
			return "None"
		else:
			return self.hours_set.all().aggregate(sum=Sum('hours_num'))

	@property
	def last_activity(self):
		if self.hours_set.all().order_by('-id').first() is None:
			return "None"
		else:
			return self.hours_set.all().order_by('-id').first().date
	
	def update(self):
		self.date_updated = timezone.now()
		self.save()
	
	def __str__(self):
		return (self.last_name) + ', ' + (self.first_name)



class Hours(models.Model):
	volunteer = models.ForeignKey(Volunteer)
	date = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
	hours_num = models.PositiveSmallIntegerField()
	volunteer_activity = models.CharField(max_length = 30, blank=True, null=True)
	
	def __str__(self):
		return str(self.volunteer) + ' ' + str(self.date) + ' ' + str(self.volunteer_activity)

class VolunteerGroup(models.Model):
	group_org = models.CharField(max_length = 25, blank=True, null=True)
	num_volunteers = models.SmallIntegerField(blank=True, null=True)
	date = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
	hours_num = models.PositiveSmallIntegerField()
	volunteer_activity = models.CharField(max_length = 30, blank=True, null=True)

	@property
	def total_group_hours(self):
		hours = self.num_volunteers * self.hours_num
		return hours

	def __str__(self):
		return str(self.group_org) + ' ' + str(self.date)