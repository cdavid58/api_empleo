from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Create_Publication/$',Create_Publication,name="Create_Publication"),
	url(r'^Get_List_Application/$',Get_List_Application,name="Get_List_Application"),
	url(r'^Applicat_Publication/$',Applicat_Publication,name="Applicat_Publication"),
	url(r'^All_List_Application/$',All_List_Application,name="All_List_Application"),
	url(r'^remove_user_from_applicant/$',remove_user_from_applicant,name="remove_user_from_applicant"),
	url(r'^Get_Publication/$',Get_Publication,name="Get_Publication"),
	url(r'^All_List_Application_Company/$',All_List_Application_Company,name="All_List_Application_Company"),
]