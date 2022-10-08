from django.db import models
from ckeditor.fields import RichTextField
import datetime


# Create your models here.
x = datetime.datetime.now()
class Blog(models.Model):
    title = models.CharField(max_length=450)
    url =  models.SlugField(max_length=300,default='none')
    date  =  models.CharField(max_length=200,default=x.strftime('%Y %b %d'))
    content = RichTextField()
    
    