from setting.models import Municipalities
from django.db import models


class Type_Document(models.Model):
    name = models.CharField(max_length = 35)

    def __str__(self):
        return self.name

class Type_Study(models.Model):
    name = models.CharField(max_length = 35)

    def __str__(self):
        return self.name

class Question(models.Model):
    question = models.CharField(max_length = 150)

    def __str__(self):
        return self.question

class User(models.Model):
    type_document = models.ForeignKey(Type_Document, on_delete = models.CASCADE)
    cc = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=20)
    second_surname = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(unique=True)
    psswd = models.CharField(max_length = 20)
    phone_1 = models.CharField(max_length=12)
    phone_2 = models.CharField(max_length=12, null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    verified = models.BooleanField(default=False)
    registration_date = models.DateTimeField(auto_now_add=True)
    birthdate = models.CharField(max_length = 13, null=True, blank=True)
    municipalities = models.ForeignKey(Municipalities, on_delete = models.CASCADE, null=True, blank=True)
    type_user = models.IntegerField(default= 1)
    description = models.TextField(null = True, blank = True)
    photo_profile = models.ImageField(upload_to = "Profile_User", default="Profile_User/without_logo.png", null = True, blank = True)
    photo_cover = models.ImageField(upload_to = "Cover_User", default="Cover_User/without_logo.png", null = True, blank = True)

    def __str__(self):
        return f"{self.first_name} {self.surname}"

class Response(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    response = models.CharField(max_length = 255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.question}"

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hv = models.TextField(null=True, blank = True)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Document for {self.user}"

    @classmethod
    def create_from_base64(cls, user, pdf_base64):
        if pdf_base64:
            document = cls(user=user, hv=pdf_base64)
            document.save()
            return document
        else:
            return None

class Work_Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length = 150)
    position = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    description = models.TextField()
    _from = models.DateField(null = True, blank = True)
    _to = models.DateField(null = True, blank = True)
    active = models.BooleanField(default = False)

    @classmethod
    def Create_Work_Experience(cls,data):
        register = cls(
            user = User.objects.get(pk = data['pk_user']),
            company = data['company'],
            position = data['position'],
            city = data['city'],
            description = data['description'],
            _from = data['from'],
            _to = data['to'],
            active = data['active'],
        )
        register.save()


class Studies(models.Model):
    institute = models.CharField(max_length = 150)
    title = models.CharField(max_length = 255)
    _from = models.DateField(null = True, blank = True)
    _to = models.DateField(null = True, blank = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @classmethod
    def Create_Studies(cls,data):
        register = cls(
            institute = data['institute'],
            title = data['title'],
            _from = data['_from'],
            _to = data['_to'],
            user = User.objects.get(pk = data['user'])
        )
        register.save()
