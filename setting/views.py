from django.http import HttpResponse, JsonResponse, FileResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from setting.models import Municipalities
from django.db import IntegrityError
from .models import *
import json
from .constants import *



@api_view(['POST'])
def Create_Municipalities(name):
	result = False
	Create_Area()
	Create_Lenguage()
	with open('data.json', 'r', encoding='utf-8') as file:
	    data = json.load(file)

	for i in data['rows']:
		try:
			m = Municipalities.objects.get(name = i['name'])
		except Municipalities.DoesNotExist:
			m = None
		if m is None:
			Municipalities(name = i['name']).save()
			result = True		
	return Response({'result':result})

def Create_Lenguage():
	for i in LENGUAGES:
		try:
			m = Languages.objects.get(name = i)
		except Languages.DoesNotExist:
			m = None
		if m is None:
			Languages(
				name = i
			).save()

def Create_Area():
	for i in DATA:
		try:
			m = Area.objects.get(name = i)
		except Area.DoesNotExist:
			m = None
		if m is None:
			Area(
				name = i
			).save()

@api_view(['GET'])
def Get_Area(request):
	return Response([
		{
			'pk':i.pk,
			'name':i.name
		}
		for i in Area.objects.all()
	])

@api_view(['GET'])
def Get_City(request):
	return Response([
		{
			'pk':i.pk,
			'name':i.name
		}
		for i in Municipalities.objects.all()
	])

@api_view(['GET'])
def Type_Contracts(request):
	return Response([
		{
			'pk':i.pk,
			'name':i.name
		}
		for i in Type_Contract.objects.all()
	])

@api_view(['GET'])
def Workdays(request):
	return Response([
		{
			'pk':i.pk,
			'name':i.name
		}
		for i in Workday.objects.all()
	])

@api_view(['GET'])
def Workplaces(request):
	return Response([
		{
			'pk':i.pk,
			'name':i.name
		}
		for i in Workplace.objects.all()
	])

@api_view(['GET'])
def Minimum_Studiess(request):
	return Response([
		{
			'pk':i.pk,
			'name':i.name
		}
		for i in Minimum_Studies.objects.all()
	])

@api_view(['GET'])
def languages(request):
	return Response([
		{
			'pk':i.pk,
			'name':i.name
		}
		for i in Languages.objects.all()
	])

@api_view(['GET'])
def Languages_Levels(request):
	return Response([
		{
			'pk':i.pk,
			'name':i.name
		}
		for i in Languages_Level.objects.all()
	])















