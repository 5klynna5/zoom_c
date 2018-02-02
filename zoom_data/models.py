from django.db import models
from django.utils import timezone
from datetime import datetime
from django.db.models import Sum, Count

class Resident(models.Model):
	resident_id = models.AutoField(primary_key=True)
	resident_first_name = models.CharField(max_length=20)
	resident_last_name = models.CharField(max_length=20)
	resident_move_in = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
	household = models.ForeignKey('Household')
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

	INSURANCE_CHOICES = (
		('NONE', 'None'),
		('PRIVATE', 'Private'),
		('MEDICAID', 'Medicaid'),
		('OTHER', 'Other Insurance'),
	)

	health_ins = models.CharField(max_length = 8, choices=INSURANCE_CHOICES, blank=True, null=True)


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

	@property
	def age(self):
		import datetime
		return int((datetime.date.today() - self.dob).days / 365.25  )
	
	@property
	def annual(self):
		return self.annual_set.all().order_by('-self_cert_date').first()

	@property
	def length_of_stay(self):
		import datetime
		if self.household.exit_date is None:
			return (datetime.date.today() - self.resident_move_in).days
		else:
			return (self.household.exit_date - self.resident_move_in).days
	
	@property
	def case_notes(self):
		return self.casenotes_set.all()

	def __str__(self):
		return (self.resident_last_name) + ', ' + (self.resident_first_name)

class Contact(models.Model):
	contact_resident = models.ForeignKey('Resident')
	resident_phone = models.CharField( max_length=10, blank=True, null=True)
	resident_email = models.EmailField(blank=True, null=True)
	mailing_address_line_one = models.CharField(max_length = 40, blank=True, null=True)
	mailing_address_line_two = models.CharField(max_length = 40, blank=True, null=True)
	mailing_address_city = models.CharField(max_length = 15, blank=True, null=True)
	##see if django field to make this easier / validated
	mailing_address_state = models.CharField(max_length = 2, blank=True, null=True)
	mailing_address_zip = models.SmallIntegerField(blank = True, null=True)

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

	@property
	def most_recent_progress(self):
		return self.progress_set.all().order_by('-date_progress').first()

	def __str__(self):
		return str(self.goal_date)+" : "+ str(self.goal_name)

class Household(models.Model):
	household_name = models.CharField(max_length = 20, blank=True, null=True)
	unit_num = models.PositiveSmallIntegerField(blank=True, null=True)
	move_in_date = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.", blank=True, null=True)

	UNIT_CHOICES = (
		('SH_ONE_BEDROOM', 'One Bedroom'),
		('SH_MARIF', 'MARIF'),
		('SH_STUDIO', 'Studio'),
	)
	
	unit_type = models.CharField(max_length = 14, choices=UNIT_CHOICES, blank=True, null=True)
	exit_date = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.", blank=True, null=True)
	
	@property
	def hoh(self):
		return self.resident_set.all()
	
	@property
	def children(self):
		return self.child_set.all()

	@property
	def exit_interview(self):
		return self.exitinterview_set.all().first()
	
	@property
	def length_of_stay(self):
		import datetime
		if self.exit_date is None:
			return (datetime.date.today() - self.move_in_date).days
		else:
			return (self.exit_date - self.move_in_date).days
	
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
	move_in_date = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.", blank=True, null=True)

	@property
	def activities(self):
		return self.childattendance_set.all()

	@property
	def length_of_stay(self):
		import datetime
		if self.household.exit_date is None:
			return (datetime.date.today() - self.move_in_date).days
		else:
			return (self.household.exit_date - self.move_in_date).days

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
	def attendee_list(self):
		return self.attendance_set.all().order_by('resident')

	@property
	def child_attendances(self):
		return self.childattendance_set.all().count()

	@property
	def child_attendee_list(self):
		return self.childattendance_set.all()

	@property
	def surveys(self):
		return self.activitysurvey_set.all()

	def __str__(self):
		return str(self.activity_name)


class Attendance(models.Model):
	resident = models.ForeignKey(Resident)
	activity = models.ForeignKey(Activity)
	complete_date = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.", blank=True, null=True)

	@property
	def follow_up(self):
		return self.followup_set.all().first()

	def __str__(self):
		return str(self.activity)

class FollowUp(models.Model):
	attendance = models.ForeignKey(Attendance)
	follow_up_date = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.", blank=True, null=True)
	apply_goals = models.TextField(blank=True, null=True)
	use_skills = models.TextField(blank=True, null=True)
	compare_before = models.TextField(blank=True, null=True)
	affected_life = models.TextField(blank=True, null=True)

	def __str__(self):
		return str(self.attendance)
	
class ActivitySurvey(models.Model):
	activity = models.ForeignKey(Activity)
	survey_complete_date = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.", blank=True, null=True)

	NEEDS_IMPROVE = models.BooleanField(default = False)
	INTERESTING = models.BooleanField(default = False)
	INCENTIVE = models.BooleanField(default = False)
	ADVOCATE = models.BooleanField(default = False)
	OTHER_REC = models.BooleanField(default = False)
	PEOPLE = models.BooleanField(default = False)

	KNOWLEDGE_CHOICES = (
		('NO', 'No knowledge'),
		('A_LITTLE', 'A little knowledge'),
		('SOME', 'Some knowledge'),
		('A_LOT', 'A lot of knowledge'),
		('ALL', 'All the knowledge I need'),
	)
	
	knowledge_before = models.CharField(max_length = 8, choices = KNOWLEDGE_CHOICES, blank=True, null=True)
	knowledge_after = models.CharField(max_length = 8, choices = KNOWLEDGE_CHOICES, blank=True, null=True)

	CONFIDENT_CHOICES = (
		('NOT_AT_ALL', 'Not at all confident'),
		('SIGHTLY', 'Slightly confident'),
		('SOMEWHAT', 'Somewhat confident'),
		('MODERATELY', 'Moderately confident'),
		('EXTREMELY', 'Extremely confident'),
	)

	confident_before = models.CharField(max_length = 10, choices = CONFIDENT_CHOICES, blank=True, null=True)
	confident_after = models.CharField(max_length = 10, choices = CONFIDENT_CHOICES, blank=True, null=True)

	comments = models.TextField(blank=True, null=True)

	UNIT_CHOICES = (
		('SUPPORTIVE', 'Supportive Housing'),
		('MARIF', 'MARIF'),
		('STUDIO', 'Studio'),
	)
	
	unit_type = models.CharField(max_length = 10, choices=UNIT_CHOICES, blank=True, null=True)

	def __str__(self):
		return str(self.activity) + 'survey' + str(self.pk)

class ChildAttendance(models.Model):
	child = models.ForeignKey(Child)
	activity = models.ForeignKey(Activity)
	complete_date = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.", blank=True, null=True)

	def __str__(self):
		return str(self.activity)

class ExitInterview(models.Model):
	household = models.ForeignKey(Household)
	exit_interview_date = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.", blank=True, null=True)

	SHELTER_CHOICES = (
		('FRIEND_FAMILY','Staying with friend or family'),
		('SECTION_8', 'Section 8 Housing'),
		('MARKET_RATE', 'Market Rate Housing'),
		('OTHER_PROGRAM', 'Other Housing Program'),
		('SHELTER','Shelter'),
		('UNKNOWN', 'Do not know'),
		('OTHER', 'Other'),
		('PREFER_NOT_SAY', 'Prefer not to say'),
	)

	living_next = models.CharField(max_length = 15, choices = SHELTER_CHOICES, blank=True, null=True)
	living_next_other = models.CharField(max_length = 30, blank=True, null=True)

	goal_one_name = models.CharField(max_length = 30, blank=True, null=True)

	PROGRESS_CHOICES = (
		('less than 25%', 'less than 25%'),
		('25%', '25%'),
		('50%', '50%'),
		('75%', '75%'),
		('100%', '100%'),
	)

	goal_one_progress = models.CharField(max_length=13, choices=PROGRESS_CHOICES, blank=True, default = "less than 25%")
	goal_one_status = models.TextField(blank=True)

	goal_two_name = models.CharField(max_length = 30, blank=True, null=True)
	goal_two_progress = models.CharField(max_length=13, choices=PROGRESS_CHOICES, blank=True, default = "less than 25%")
	goal_two_status = models.TextField(blank=True)

	goals_future = models.TextField(blank=True)

	why_leaving = models.TextField(blank=True)

	most_helpful = models.TextField(blank=True)

	not_helpful = models.TextField(blank=True)

	advice_resident = models.TextField(blank=True)

	advice_staff = models.TextField(blank=True)

	def __str__(self):
		return str(self.household)

class Annual(models.Model):
	resident = models.ForeignKey(Resident)
	self_cert_date = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.", blank=True, null=True)
	
	annual_income = models.SmallIntegerField(blank=True, help_text = "in U.S. dollars")

	YES_NO_CHOICES = {
		('Yes', 'YES'),
		('No', 'NO'),
	}

	student_status = models.CharField(max_length = 3, choices = YES_NO_CHOICES, blank=True, null=True)

	employment_status = models.CharField(max_length = 3, choices = YES_NO_CHOICES, blank=True, null=True)

	def __str__(self):
		return str(self.resident) + ' ' + str(self.self_cert_date)

class CaseNotes(models.Model):
	resident = models.ForeignKey(Resident)
	date_notes = models.DateField(help_text="Enter the date notes were taken. Please use the following format: <em>YYYY-MM-DD</em>.", blank=True, null=True)

	notes = models.TextField(blank=True, null=True)

	def __str__(self):
		return str(self.resident) + ' ' + str(self.date_notes)
