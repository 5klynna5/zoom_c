from django.db import models

class Event(models.Model):
    date = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.", blank=True, null=True)
    title = models.CharField(max_length = 25, null=True, blank=True)
    num_attendees = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.title)

class Grant(models.Model):
    funder = models.CharField(max_length = 20, blank=True, null=True)
    grant_title = models.CharField(max_length = 20, blank=True, null=True)
    date_applied = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.", blank=True, null=True)
    date_funds_received = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.", blank=True, null=True)
    grant_start_date = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.", blank=True, null=True)
    grant_end_date = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.", blank=True, null=True)
    funding_requirements = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.grant_title) + ' | ' + str(self.funder) + ' ' + str(self.grant_start_date) + ' - ' + str(self.grant_end_date)
