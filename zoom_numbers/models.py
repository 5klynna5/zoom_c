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
