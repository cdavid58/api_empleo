from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Create_User/$',Create_User,name="Create_User"),
	url(r'^Get_Data_User/$',Get_Data_User,name="Get_Data_User"),
	url(r'^Get_User/$',Get_User,name="Get_User"),
	url(r'^Update_Information_Persons/$',Update_Information_Persons,name="Update_Information_Persons"),
	url(r'^Create_Work_Experiences/$',Create_Work_Experiences,name="Create_Work_Experiences"),
	url(r'^Delete_Work_Experiences/$',Delete_Work_Experiences,name="Delete_Work_Experiences"),
	url(r'^Create_Studies/$',Create_Studies,name="Create_Studies"),
]