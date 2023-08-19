from django.http import HttpResponse, JsonResponse, FileResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from setting.models import Municipalities
from django.db import IntegrityError
from .models import *
import json

@api_view(['POST'])
def Create_User(request):
	data = request.data
	result = False
	pk = 0
	try:
		user = User.objects.get(cc=data['cc'] ,email = data['email'])
	except User.DoesNotExist:
		user = None
	if user is None:
		user = User(
			type_document = Type_Document.objects.get(pk = data['type_document']),
			cc = data['cc'],
			first_name = data['first_name'],
			surname = data['surname'],
			email = data['email'],
			psswd = data['psswd'],
			phone_1 = data['phone_1']
		)
		user.save()
		result = True
	return JsonResponse({'result':result,'pk_user':user.pk})

@api_view(['POST'])
def Compress_PDF(request):
	data = request.data
	result = False
	try:
		user = User.objects.get(pk=data['pk'])
	except User.DoesNotExist:
		user = None
	if user is not None:
		base64_string = data['base64_string']
		document = Document.create_from_base64(user, base64_string)
		if document is not None:
			result = True
	return Response({'result': result})



@api_view(['GET'])
def Get_Data_User(request):
	data = request.data
	try:
		user = User.objects.get(email = data['email'], psswd = data['psswd'])
	except User.DoesNotExist:
		user = None
	value = False
	pk_user = 0
	type_user = 0


	message = "El usuario no existe"
	if user is not None:
		if not user.verified:
			message = "No tiene la cuenta verificada"
		else:
			value = True
			pk_user = user.pk,
			type_user =  user.type_user

	result = {
		"result":value,
		"pk_user": pk_user,
		"type_user":type_user,
		"message":message
	}

	return JsonResponse(result)


@api_view(['GET'])
def Get_User(request):
	i = User.objects.get(pk = request.data['pk_user'])
	data = {
		"cc": i.cc,
		"first_name":i.first_name,
		"surname":i.surname,
		"second_surname":i.second_surname,
		"email":i.email,
		"phone_1":i.phone_1,
		"phone_2":i.phone_2,
		"address":i.address,
		"birthdate":i.birthdate,
		"municipalities":i.municipalities.name,
		'description':i.description,
	}
	try:
		doc = Document.objects.get(user = i)
		data['document'] = {
			'pk_doc':doc.pk,
			'doc':doc.hv
		}
	except Document.DoesNotExist:
		data['document'] = []

	try:
		we = Work_Experience.objects.filter(user = i)
		data['Work_Experience'] = [
			{
				'pk_work_experience' : i.pk,
				'company' : i.company,
				'position' : i.position,
				'city' : i.city,
				'description' : i.description,
				'_from' : i._from,
				'_to' : i._to,
				'active' : i.active
			}
			for i in we
		]
	except Exception as e:
		data['Work_Experience'] = []


	try:
		data['studies'] = [
			{
				"pk":i.pk,
				"institute":i.institute,
				"title":i.title,
				"from":i._from,
				"to":i._to,
			}
			for i in Studies.objects.filter(user = i)
		]
	except Studies.DoesNotExist:
		data['studies'] = []

	print(data)

	return JsonResponse(data)


@api_view(['PUT'])
def Update_Information_Persons(request):
	data = request.data
	result = False
	user = None
	try:
		user = User.objects.get(pk = data['pk_user'])
		user.first_name = data['name']
		user.surname = data['surname']
		user.second_surname = data['second_surname']
		user.email = data['email']
		user.phone_1 = data['phone_1']
		user.phone_2 = data['phone_2']
		user.birthdate = data['birthdate']
		user.municipalities = Municipalities.objects.get(name = data['municipalities'])
		user.description = data['description']
		user.save()
		result = True
	except Exception as e:
		pass

	if data['doc'] is not None and data['doc'] != "None":
		try:
			doc = Document.objects.get(user = user)
		except Document.DoesNotExist as e:
			doc = None

		if doc is None:
			doc = Document.create_from_base64(user, data['doc'])
		else:
			doc.hv = data['doc']
			doc.save()

	return JsonResponse({'result':result})


@api_view(['POST'])
def Create_Work_Experiences(request):
	data = request.data
	result = False
	try:
		w_e = Work_Experience.Create_Work_Experience(data)
		result = True
	except Exception as e:
		print(e)
	return JsonResponse({'result':result})

@api_view(['POST'])
def Create_Studies(request):
	data = request.data
	result = False
	try:
		w_e = Studies.Create_Studies(data)
		result = True
	except Exception as e:
		print(e)
	return JsonResponse({'result':result})



@api_view(['DELETE'])
def Delete_Work_Experiences(request):
	result = False
	try:
		Work_Experience.objects.get(pk = request.data['pk_work_experience']).delete()
		result = True
	except Work_Experience.DoesNotExist as e:
		pass
	return JsonResponse({'result':result})

