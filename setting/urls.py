from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Create_Municipalities/$',Create_Municipalities,name="Create_Municipalities"),
	url(r'^Get_Area/$',Get_Area,name="Get_Area"),
	url(r'^Get_City/$',Get_City,name="Get_City"),
	url(r'^Type_Contract/$',Type_Contracts,name="Type_Contract"),
	url(r'^Workday/$',Workdays,name="Workday"),
	url(r'^Workplace/$',Workplaces,name="Workplace"),
	url(r'^Minimum_Studiess/$',Minimum_Studiess,name="Minimum_Studiess"),
	url(r'^languages/$',languages,name="languages"),
	url(r'^Languages_Levels/$',Languages_Levels,name="Languages_Levels"),
]