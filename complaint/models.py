from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class complaint(models.Model):
    name=models.CharField(max_length=50,default="",null=False)
    father_name=models.CharField(max_length=50,default="",null=False)
    mother_name=models.CharField(max_length=50,default="",null=False)
    address=models.CharField(max_length=200,default="",null=False)
    gender=models.CharField(max_length=50,default="",null=False)
    complain=models.CharField(max_length=200,default="",null=False)
    email=models.CharField(max_length=50,default="",null=False)
    contact_no=PhoneNumberField(blank=True)
    
