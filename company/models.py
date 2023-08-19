from django.db import models

class Company(models.Model):
	nit = models.IntegerField(unique = True)
	name = models.CharField(max_length = 50,unique = True)
	email = models.EmailField(unique = True)
	phone_1 = models.CharField(max_length = 15)
	phone_2 = models.CharField(max_length = 15, blank = True, null = True)
	verified = models.BooleanField(default=False)
	registration_date = models.DateTimeField(auto_now_add=True)
	logo = models.ImageField(upload_to = "Logo_Company", default="Logo_Company/without_logo.png", blank = True, null = True)
	password = models.CharField(max_length = 20, null= True, blank = True)
	type_user = models.IntegerField(default = 2)
	
	def __str__(self):
		return f"{self.nit} - {self.name}"

