from django.db import models
from datetime import datetime
from django.core.validators import validate_slug
# Create your models here.

class products(models.Model):

	productname = models.CharField(max_length=250)
	price = models.CharField(max_length=250)
	category = models.TextField(null=True,blank=True)
	image = models.FileField(blank=True,upload_to='productImage/%Y/%m/%d')
	datecreated = models.DateField(default=datetime.now,blank=True)

class productnew(models.Model):

	productname = models.CharField(max_length=250)
	price = models.CharField(max_length=250)
	category = models.TextField(null=True,blank=True)
	image = models.FileField(blank=True,upload_to='productImage/%Y/%m/%d')
	datecreated = models.DateField(default=datetime.now,blank=True)

		
