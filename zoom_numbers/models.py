from django.db import models
from django.utils import timezone

class YMCA(models.Model):

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

	month = models.CharField(max_length = 3, choices = MONTH_CHOICES)
	year = models.PositiveSmallIntegerField()
	number_visits = models.PositiveSmallIntegerField()

	def __str__(self):
		return self.month + ", " + str(self.year)

class FoodShelf(models.Model):

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

	month = models.CharField(max_length = 3, choices = MONTH_CHOICES)
	year = models.PositiveSmallIntegerField()
	number_visits = models.PositiveSmallIntegerField()

	def __str__(self):
		return str(self.month) + " " + str(self.year)


class PoliceCalls(models.Model):
	
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

	month = models.CharField(max_length = 3, choices = MONTH_CHOICES)
	year = models.PositiveSmallIntegerField()

	domestic = models.PositiveSmallIntegerField(blank=True, null=True)
	disturbance = models.PositiveSmallIntegerField(blank=True, null=True)
	drug = models.PositiveSmallIntegerField(blank=True, null=True)
	violence = models.PositiveSmallIntegerField(blank=True, null=True)
	assault = models.PositiveSmallIntegerField(blank=True, null=True)
	theft = models.PositiveSmallIntegerField(blank=True, null=True)
	health = models.PositiveSmallIntegerField(blank=True, null=True)
	other = models.PositiveSmallIntegerField(blank=True, null=True)

	@property
	def total_calls(self):
		calls_sum = 0
		for item in [self.domestic, self.disturbance, self.drug, self.violence, self.assault, self.theft, self.health, self.other]:
			if item is not None:
				calls_sum = calls_sum + item
			else:
				calls_sum = calls_sum + 0
		return calls_sum
		
	def __str__(self):
		return str(self.month) + " " + str(self.year)

class QuestionMonth(models.Model):

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

	month = models.CharField(max_length = 3, choices = MONTH_CHOICES)
	year = models.PositiveSmallIntegerField()

	question = models.CharField(max_length = 50)

	category_one = models.CharField(max_length = 25)
	category_one_count = models.SmallIntegerField()

	@property
	def cat_one_percent(self):
		total_count = self.category_one_count + self.category_two_count + self.category_three_count + self.category_four_count
		perc = (self.category_one_count / total_count) * 100
		return "{0:0.1f}".format(perc)

	category_two = models.CharField(max_length = 25)
	category_two_count = models.SmallIntegerField()

	@property
	def cat_two_percent(self):
		total_count = self.category_one_count + self.category_two_count + self.category_three_count + self.category_four_count
		perc = (self.category_two_count / total_count) * 100
		return "{0:0.1f}".format(perc)

	category_three = models.CharField(max_length = 25)
	category_three_count = models.SmallIntegerField()

	@property
	def cat_three_percent(self):
		total_count = self.category_one_count + self.category_two_count + self.category_three_count + self.category_four_count
		perc = (self.category_three_count / total_count) * 100
		return "{0:0.1f}".format(perc)

	category_four = models.CharField(max_length = 25)
	category_four_count = models.SmallIntegerField()

	@property
	def cat_four_percent(self):
		total_count = self.category_one_count + self.category_two_count + self.category_three_count + self.category_four_count
		perc = (self.category_four_count / total_count) * 100
		return "{0:0.1f}".format(perc)

	def __str__(self):
		return str(self.question)