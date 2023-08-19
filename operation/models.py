from company.models import Company
from user.models import User
from setting.models import *
from django.db import models


class Publication(models.Model):
	_id = models.CharField(max_length = 30, unique=True)
	offer_title = models.CharField(max_length = 150)
	area = models.ForeignKey(Area, on_delete = models.CASCADE)
	description = models.TextField()
	municipalities = models.ForeignKey(Municipalities, on_delete = models.CASCADE, related_name='municipalities')
	workday = models.ForeignKey(Workday, on_delete = models.CASCADE, related_name='workday')
	workplace = models.ForeignKey(Workplace, on_delete = models.CASCADE, related_name='workplace')
	type_contract = models.ForeignKey(Type_Contract, on_delete = models.CASCADE, related_name='type_contract')
	salary = models.FloatField()
	date_hire = models.CharField(max_length = 13)
	number_vacancies = models.IntegerField()
	years_experience = models.FloatField()
	age_start = models.IntegerField()
	age_end = models.IntegerField()
	minimum_studies = models.ForeignKey(Minimum_Studies, on_delete = models.CASCADE, related_name='minimum_studies')
	languages = models.ForeignKey(Languages, on_delete = models.CASCADE, related_name='languages')
	languages_level = models.ForeignKey(Languages_Level, on_delete = models.CASCADE, related_name='languages_level')
	driving_license = models.ManyToManyField(Driving_License, related_name='driving_license')
	availability_travel = models.BooleanField(default = True)
	change_residence = models.BooleanField(default = True)
	registration_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now_add=True)
	company = models.ForeignKey(Company, on_delete = models.CASCADE, related_name='company')

class Applicant(models.Model):
	user = models.ManyToManyField(User, related_name='publications_applied')
	publication = models.ForeignKey(Publication, on_delete = models.CASCADE, related_name='publications')
	applicant_date = models.DateTimeField(auto_now_add=True)



