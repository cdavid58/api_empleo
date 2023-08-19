from django.db import models

class Area(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Municipalities(models.Model):
    name = models.CharField(max_length = 35)

    def __str__(self):
        return self.name
	
class Workday(models.Model):
    name = models.CharField(max_length = 35, unique = True)

    def __str__(self):
        return self.name

class Workplace(models.Model):
    name = models.CharField(max_length = 35, unique = True)

    def __str__(self):
        return self.name

class Type_Contract(models.Model):
    name = models.CharField(max_length = 50, unique = True)

    def __str__(self):
        return self.name

class Minimum_Studies(models.Model):
    name = models.CharField(max_length = 40, unique = True)

    def __str__(self):
        return self.name

class Languages(models.Model):
    name = models.CharField(max_length = 40, unique = True)

    def __str__(self):
        return self.name

class Languages_Level(models.Model):
    name = models.CharField(max_length = 40, unique = True)

    def __str__(self):
        return self.name

class Driving_License(models.Model):
    name = models.CharField(max_length = 40, unique = True)

    def __str__(self):
        return self.name

