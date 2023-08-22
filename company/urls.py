from django.conf.urls import url
from .views import *


urlpatterns=[
	url(r'^Create_Company/$',Create_Company,name="Create_Company"),
	url(r'^Login/$',Login,name="Login"),
	url(r'^verified_company_ready/$',verified_company_ready,name="verified_company_ready"),
]