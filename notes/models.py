from django.db import models
from django.utils import timezone
from django import forms
from django.core.urlresolvers import reverse
  
year_choices = (
        ( 1  , 'First' ),
        ( 2  , 'Second'),
        ( 3  , 'Third' ),
        ( 4  , 'Fourth')
  )
branch_choices = (
        ( 'IT','IT'  ),
        ( 'EE','EE'  ),
        ( 'CSE','CSE'),
        ( 'EC','EC'  ),
        ( 'ME','ME'  ),
        ( 'CE','CE'  ),
  )


subject_choices = (
        ( 'DS' , 'Data Structure'  ),
        ( 'OS' , 'Operating sytem' ),
        ( 'EC' , 'Ecomomics'       ),
        ( 'Thermo' , 'Thermo'      ),
  )

def generate_picture_name(instance, filename):
    url = "images/{0}_{1}_{2}_{3}.jpg".format(
        instance.branch, instance.year, instance.subject_name, instance.unit)
    return url


class subjects(models.Model):
  year=models.IntegerField(choices=year_choices)
  branch=models.CharField(max_length=100)
  subjects=models.CharField(max_length=50)



class Note(models.Model):
  unit_choices = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'),(8,'8'),(9,'9'),(10,'10'))
  branch = models.CharField(max_length=55,choices=branch_choices)
  year = models.IntegerField(choices = year_choices)
  subject_name = models.CharField(choices=subject_choices,max_length=10)
  unit = models.IntegerField(choices=unit_choices)
  picture = models.ImageField(upload_to = generate_picture_name)
  

  def __str__(self):
    return self.subject_name