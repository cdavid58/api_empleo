from django.http import HttpResponse, JsonResponse, FileResponse
from emaills.send_emails import Send_Email_Verified_Company
from rest_framework.decorators import api_view
from django.utils.crypto import get_random_string
from django.shortcuts import render, redirect
from rest_framework.response import Response
from setting.models import Municipalities, Tokens
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
		)
		company.save()
		result = True
		token = get_random_string(length=60)
		Tokens(token=token).save()
		Send_Email_Verified_Company(company.pk, token)
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

@api_view(['POST'])
def verified_company_ready(request):
	data = request.data
	result = False
	try:
		company = Company.objects.get(pk = data['pk_company'])
		Tokens.objects.get(token = data['token']).delete()
		company.verified = True
		company.save()
		result = True
	except Exception as e:
		print(e)
	return Response({'result':result})
