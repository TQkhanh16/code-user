from django.db import models

# Create your models here.
class User(models.Model):

    userName = models.CharField(max_length=255,default = None)
    passWord = models.CharField(max_length=255,default = None)
    firstName = models.CharField(max_length=255,default = None)
    lastName = models.CharField(max_length=255,default = None)
    email = models.CharField(max_length=255,default = None)
    birthday = models.DateField(default = None)
    position = models.CharField(max_length=255,default = None)
    isAdmin = models.BooleanField(default = None)
    departmentName = models.CharField(max_length=255,default = None)
    describe = models.CharField(max_length=255,default = None)
    phoneNumber = models.CharField(max_length=255,default = None)

    def _str_(self):
        return self.userName