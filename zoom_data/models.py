from django.db import models
from django.utils import timezone
from datetime import datetime
from django.db.models import Sum, Count

class Resident(models.Model):
	resident_id = models.AutoField(primary_key=True)
	resident_first_name = models.CharField(max_length=20)
	resident_last_name = models.CharField(max_length=20)
	resident_move_in = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
	household = models.ForeignKey('Household', blank=True, null=True)

	GENDER_CHOICES = (
		('FEMALE', 'Female'),
		('MALE', 'Male'),
		('ALT', 'Another gender'),
	)

	gender = models.CharField(max_length = 6, choices = GENDER_CHOICES, blank=True, null=True)
	
	RACE_CHOICES = (
		('AFRICAN_AMERICAN', 'African American'),
		('WHITE', 'White'),
		('MULTIRACIAL', 'Multiracial'),
		('AMER_INDIAN', 'American Indian'),
		('PAC_ISLANDER', 'Native Hawaiian or Pacific Islander'),
		('ASIAN_AMERICAN', 'Asian American'),
	)

	race = models.CharField(max_length = 16, choices = RACE_CHOICES, blank=True, null=True)

	ETHNICITY_CHOICES = (
		('HISPANIC', 'Hispanic'),
		('NON-HISPANIC', 'Non-Hispanic'),
	)

	ethnicity = models.CharField(max_length = 12, choices = ETHNICITY_CHOICES, blank=True, null=True)

	INSURANCE_CHOICES = (
		('NONE', 'None'),
		('PRIVATE', 'Private'),
		('MEDICAID', 'Medicaid'),
		('OTHER', 'Other Insurance'),
	)

	health_ins = models.CharField(max_length = 8, choices=INSURANCE_CHOICES, blank=True, null=True)

	resident_exit  = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.", null=True, blank=True)

	@property
	def goals(self):
		return self.goal_set.all()

	@property
	def contact_preferred(self):
		if self.contact_set.all().order_by('-id').first() is None:
			return "None"
		else:
			return self.contact_set.all().order_by('-date_updated').first()
	
	@property
	def activities(self):
		return self.attendance_set.all()
	

	def __str__(self):
		return (self.resident_last_name) + ', ' + (self.resident_first_name)

class Contact(models.Model):
	contact_resident = models.ForeignKey('Resident')
	resident_phone = models.CharField( max_length=10, blank=True, null=True)
	resident_email = models.EmailField(blank=True, null=True)

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
		('Facebook', 'FACEBOOK')
	}

	contact_pref = models.CharField(max_length=8, choices=CONTACT_CHOICES, blank=True, null=True)

	date_updated = models.DateTimeField(blank=True, null=True)
	
	def update(self):
		self.date_updated = timezone.now()
		self.save()
	
	def __str__(self):
		return str(self.contact_resident) + ' ' + str(self.date_updated.strftime("%m-%d-%Y"))

class Goal(models.Model):
	goal_name = models.CharField(max_length = 100)
	goal_date = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.", blank=True, null=True)
	goal_explain = models.TextField(blank=True)
	goal_resident = models.ForeignKey('Resident')

	@property
	def current_progress(self):
		if self.progress_set.all().order_by('-id').first() is None:
			return "less than 25%"
		else:
			return self.progress_set.all().order_by('-date_progress').first().percent_progress
	
	@property
	def all_progress(self):
		return self.progress_set.all().order_by('-date_progress')

	def __str__(self):
		return str(self.goal_date)+" : "+ str(self.goal_name)

class Household(models.Model):
	household_name = models.CharField(max_length = 20, blank=True, null=True)
	unit_num = models.PositiveSmallIntegerField(blank=True, null=True)
	UNIT_CHOICES = (
		('SUPPORTIVE', 'Supportive Housing'),
		('MARIF', 'MARIF'),
		('STUDIO', 'Studio'),
	)
	
	unit_type = models.CharField(max_length = 10, choices=UNIT_CHOICES, blank=True, null=True)
	
	@property
	def hoh(self):
		return self.resident_set.all()
	
	@property
	def children(self):
		return self.child_set.all()
	
	def __str__(self):
		return str(self.household_name)

class Progress(models.Model):

	PROGRESS_CHOICES = (
		('less than 25%', 'less than 25%'),
		('25%', '25%'),
		('50%', '50%'),
		('75%', '75%'),
		('100%', '100%'),
	)

	goal = models.ForeignKey('Goal')
	date_progress = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
	percent_progress = models.CharField(max_length=13, choices=PROGRESS_CHOICES, blank=True, default = "less than 25%")
	notes_progress = models.TextField(blank=True)

	def __str__(self):
		return str(self.goal) + " " + str(self.date_progress)

class Child(models.Model):
	first_name = models.CharField(max_length = 15, blank=True, null=True)
	last_name = models.CharField(max_length=15, blank=True, null=True)
	household = models.ForeignKey('Household', blank=True, null=True)
	dob = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.", blank=True, null=True)

	GENDER_CHOICES = (
		('FEMALE', 'Female'),
		('MALE', 'Male'),
		('ALT', 'Another gender'),
	)

	gender = models.CharField(max_length = 6, choices = GENDER_CHOICES, blank=True, null=True)

	RACE_CHOICES = (
		('AFRICAN_AMERICAN', 'African American'),
		('WHITE', 'White'),
		('MULTIRACIAL', 'Multiracial'),
		('AMER_INDIAN', 'American Indian'),
		('PAC_ISLANDER', 'Native Hawaiian or Pacific Islander'),
		('ASIAN_AMERICAN', 'Asian American'),
	)

	race = models.CharField(max_length = 16, choices = RACE_CHOICES, blank=True, null=True)

	ETHNICITY_CHOICES = (
		('HISPANIC', 'Hispanic'),
		('NON-HISPANIC', 'Non-Hispanic'),
	)

	ethnicity = models.CharField(max_length = 12, choices = ETHNICITY_CHOICES, blank=True, null=True)

	@property
	def activities(self):
		return self.childattendance_set.all()

	@property
	def age(self):
		import datetime
		return int((datetime.date.today() - self.dob).days / 365.25  )

	def __str__(self):
		return str(self.first_name) + " " + str(self.last_name)


class Activity(models.Model):
	activity_name = models.CharField(max_length=25)
	
	SKILL_CHOICES = (
		('FINANCE', 'Finance'),
		('PARENTING', 'Parenting'),
		('EMPLOYMENT', 'Employment'),
		('FITNESS', 'Fitness'),
	)

	skill_area = models.CharField(max_length = 15, choices=SKILL_CHOICES, blank=True, null=True)

	MONTH_CHOICES = (
		('Jan', 'January'),
		('Feb', 'February'),
		('Mar', 'March'),
		('Apr', 'April'),
		('May', 'May'),
		('Jun', 'June'),
		('Jul', 'July'),
		('Aug', 'August'),
		('Sep', 'September'),
		('Oct', 'October'),
		('Nov', 'November'),
		('Dec', 'December'),
	)

	month = models.CharField(max_length = 3, choices = MONTH_CHOICES, blank=True, null=True)
	year = models.PositiveSmallIntegerField(null=True)

	@property
	def attendances(self):
		return self.attendance_set.all().count()

	@property
	def child_attendances(self):
		return self.childattendance_set.all().count()


	def __str__(self):
		return str(self.activity_name)


class Attendance(models.Model):
	resident = models.ForeignKey(Resident)
	activity = models.ForeignKey(Activity)
	complete_date = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.", blank=True, null=True)

	def __str__(self):
		return str(self.activity)

class ChildAttendance(models.Model):
	child = models.ForeignKey(Child)
	activity = models.ForeignKey(Activity)
	complete_date = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.", blank=True, null=True)

	def __str__(self):
		return str(self.activity)



