from from_number_to_letters import Thousands_Separator
from django.utils.crypto import get_random_string
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from setting.models import Municipalities
from django.db import IntegrityError
from company.models import Company
from datetime import datetime, timezone
from setting.models import *
from user.models import User
from .models import *
import json

@api_view(['POST'])
def Create_Publication(request):
	data = request.data
	token = get_random_string(length=30)
	result = False
	try:
		p = Publication.objects.get(_id = token)
	except Publication.DoesNotExist:
		p = None

	if p is not None:
		token = get_random_string(length=30)
	try:
		p = Publication.objects.create(
			_id = token,
			offer_title = data['offer_title'],
			area = Area.objects.get(pk = data['area']),
			description = data['description'],
			municipalities = Municipalities.objects.get(pk = data['municipalities']),
			workday = Workday.objects.get(pk = data['workday']),
			workplace = Workplace.objects.get(pk = data['workplace']),
			type_contract = Type_Contract.objects.get(pk = data['type_contract']),
			salary = data['salary'],
			date_hire = data['date_hire'],
			number_vacancies = data['number_vacancies'],
			years_experience = data['years_experience'],
			age_start = data['age_start'],
			age_end = data['age_end'],
			minimum_studies = Minimum_Studies.objects.get(pk = data['minimum_studies']),
			languages = Languages.objects.get(pk = data['languages']),
			languages_level = Languages_Level.objects.get(pk = data['languages_level']),
			availability_travel = data['availability_travel'],
			change_residence = data['change_residence'],
			company = Company.objects.get(pk = data['company'])
		)
		index_of_zero = next((index for index, value in enumerate(data['driving_license']) if value == 0), None)
		if index_of_zero is not None:
		    p.driving_license.add(Driving_License.objects.get(pk = 10))
		else:
			for i in data['driving_license']:
				p.driving_license.add(Driving_License.objects.get(pk = i))
		result = True
	except Exception as e:
		print(e)

	return Response({'result':result})

@api_view(['POST'])
def remove_user_from_applicant(request):
    data = request.data
    result = False
    
    try:
    	publication = Publication.objects.get(pk = data['pk'])
    	app = Applicant.objects.get(publication = publication)
    	user = User.objects.get(pk=data['pk_user'])
    	app.user.remove(user)
    	result = True
    	if app.user.count() == 0:
    		app.delete()
    		result = True
    except (Applicant.DoesNotExist, User.DoesNotExist):
    	pass
    return Response({'result': result})

@api_view(['POST'])
def Applicat_Publication(request):
	data = request.data
	result = False
	try:
		app = Applicant.objects.get(publication = Publication.objects.get(pk=data['pk_publication']))
		app.user.add(User.objects.get(pk = data['pk_user']))
		result = True
	except Applicant.DoesNotExist as e:
		app = None

	if app is None:
		publication = Publication.objects.get(pk=data['pk_publication'])
		user = User.objects.get(pk=data['pk_user'])
		app = Applicant.objects.create(publication=publication)
		app.user.add(user)
		result = True
	return Response({'result':result})

@api_view(['GET'])
def Get_List_Application(request):
	app = Applicant.objects.all()
	data = []
	pk_user = request.data.get('pk_user')
	total_applicants = 0
	for i in app:
		user = i.user.filter(pk=pk_user).first()
		if user is not None:
			total_applicants += i.user.count()
			data.append(
				{
					'pk_application': i.pk,
					"offer_title": i.publication.offer_title,
					"area": i.publication.area.name,
					"description": i.publication.description,
					"municipalities": i.publication.municipalities.name,
					"workday": i.publication.workday.name,
					"workplace": i.publication.workplace.name,
					"type_contract": i.publication.type_contract.name,
					"salary": i.publication.salary,
					"date_hire": i.publication.date_hire,
					"number_vacancies": i.publication.number_vacancies,
					"years_experience": i.publication.years_experience,
					"age_start": i.publication.age_start,
					"age_end": i.publication.age_end,
					"minimum_studies": i.publication.minimum_studies.name,
					"languages": i.publication.languages.name,
					"languages_level": i.publication.languages_level.name,
					"driving_license": i.publication.driving_license.name,
					"availability_travel": i.publication.availability_travel,
					"change_residence": i.publication.change_residence,
					"pk_company": i.publication.company.pk,
					"nit_company": i.publication.company.nit,
					"name_company": i.publication.company.name,
					"email_company": i.publication.company.email,
					"phone_1_company": i.publication.company.phone_1,
					"phone_2_company": i.publication.company.phone_2 if i.publication.company.phone_2 != "" and i.publication.company.phone_2 is not None else None,
					"pk_user": request.data['pk_user'],
					'logo_company': f"http://127.0.0.1:9090{i.publication.company.logo.url}"
				}
			)
	return Response({'data':data, 'number_applications':total_applicants})

def Calculate_Value(Time):
    fecha_dada = datetime.strptime(str(Time), "%Y-%m-%d %H:%M:%S.%f%z")
    fecha_actual = datetime.now(timezone.utc)
    diferencia = fecha_actual - fecha_dada

    dias = diferencia.days
    segundos_totales = diferencia.seconds
    horas, segundos = divmod(segundos_totales, 3600)
    minutos, segundos = divmod(segundos, 60)

    message = None
    if dias > 0:
        message = f"Hace {dias} días."
    elif horas > 0:
        message = f"Hace {horas} horas."
    elif minutos > 0:
        message = f"Hace {minutos} minutos."
    else:
        message = "Hace menos de un minuto."
    return message	

@api_view(['GET'])
def All_List_Application(request):
	app = Publication.objects.all().order_by('-pk')
	data = [
		{
			'pk_application': i.pk,
			'logo_company': f"http://127.0.0.1:9090{i.company.logo.url}",
			'name_company':i.company.name,
			'title':i.offer_title,
			'place':i.municipalities.name,
			'registration_date':Calculate_Value(i.registration_date),
			'area':i.area.name,
			'description':i.description,
			'number_vacancies':i.number_vacancies,
			'salary':Thousands_Separator(i.salary),
		}
		for i in app
	]
	return Response(data)

@api_view(['GET'])
def All_List_Application_Company(request):
	app = Publication.objects.filter(company = Company.objects.get(pk = request.data['pk_company'])).order_by('-pk')
	data = [
		{
			'pk_application': i.pk,
			'logo_company': f"http://127.0.0.1:9090{i.company.logo.url}",
			'name_company':i.company.name,
			'title':i.offer_title,
			'place':i.municipalities.name,
			'registration_date':Calculate_Value(i.registration_date),
			'area':i.area.name,
			'description':i.description,
			'number_vacancies':i.number_vacancies,
			'salary':Thousands_Separator(i.salary),
		}
		for i in app
	]
	return Response(data)

@api_view(['GET'])
def Get_Publication(request):
	publication = Publication.objects.get(pk = request.data['pk'])
	data = {
		'pk_publication': publication.pk,
		"offer_title": publication.offer_title,
		"area": publication.area.name,
		"description": publication.description,
		"municipalities": publication.municipalities.name,
		"workday": publication.workday.name,
		"workplace": publication.workplace.name,
		"type_contract": publication.type_contract.name,
		"salary": Thousands_Separator(int(publication.salary)),
		"date_hire": publication.date_hire,
		"number_vacancies": publication.number_vacancies,
		"years_experience": publication.years_experience,
		"age_start": publication.age_start,
		"age_end": publication.age_end,
		"minimum_studies": publication.minimum_studies.name,
		"languages": publication.languages.name,
		"languages_level": publication.languages_level.name,
		"driving_license": publication.driving_license.name,
		"availability_travel": publication.availability_travel,
		"change_residence": publication.change_residence,
		"pk_company": publication.company.pk,
		"nit_company": publication.company.nit,
		"name_company": publication.company.name,
		"email_company": publication.company.email,
		"phone_1_company": publication.company.phone_1,
		"phone_2_company": publication.company.phone_2 if publication.company.phone_2 != "" and publication.company.phone_2 is not None else None,
		'logo_company': f"http://127.0.0.1:9090{publication.company.logo.url}"
	}
	try:
		app = Applicant.objects.get(publication = publication)
		data['list_user'] = [
			{
				'pk_user' : i.pk
			}
			for i in app.user.all()
		]
	except Applicant.DoesNotExist:
		data['list_user'] = []
	return Response(data)