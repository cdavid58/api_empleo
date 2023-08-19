from django.http import HttpResponse, JsonResponse, FileResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from setting.models import Municipalities
from django.db import IntegrityError
from .models import Company

@api_view(['POST'])
def Create_Company(request):
	data = request.data
	result = False
	try:
		company = Company.objects.get(nit = data['nit'], email = data['email'])
	except Company.DoesNotExist as e:
		company = None

	if company is None:
		company = Company(
			nit = data['nit'],
			name = data['name'],
			email = data['email'],
			phone_1 = data['phone_1'],
			password = data['psswd']
		).save()
		result = True
	return Response({'result':result})

@api_view(['GET'])
def Login(request):
	data = request.data
	try:
		user = Company.objects.get(email = data['email'], password = data['psswd'], verified = True)
	except Company.DoesNotExist as e:
		user = None
		message = e

	result = {'result':False,'message':f"La compania no existe" if user is None else ''}
	

	if user is not None:
		result = {
			"result":True,
			"pk_user": user.pk,
			"type_user":user.type_user
		}
	return Response(result)