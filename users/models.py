from django.db import models
# from home.models import Subject
# Create your models here.

SKILLS_CHOICES = ( 
    ("1", "English"), 
    ("2", "Math"), 
    ("3", "Programming"), 
    ("4", "Communication"), 
    ("5", "Psychology"), 
    ("6", "Korean Language"), 
    ("7", "Chinese"), 
    ("8", "Kind"), 
) 
CLASSES_CHOICES = ( 
    ("1", "1-Sinf"), 
    ("2", "2-Sinf"), 
    ("3", "3-Sinf"), 
    ("4", "4-Sinf"), 
    ("5", "5-Sinf"), 
    ("6", "6-Sinf"), 
    ("7", "7-Sinf"), 
    ("8", "8-Sinf"), 
    ("9", "9-Sinf"),
    ("10", "10-Sinf"),
    ("11", "11-Sinf"),
) 

class Teacher(models.Model):
    name = models.CharField(max_length=150)
    # subject = models.OneToOneField(Subject, on_delete=models.SET_NULL, null=True)
    extra_skills = models.CharField( 
        max_length = 20, 
        choices = SKILLS_CHOICES, 
        default = '8'
        ) 
    img = models.ImageField(upload_to='images/', blank=True, null=True)
    information = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.name



class Student(models.Model):
    full_name = models.CharField(max_length=50, null=True)
    sinfi = models.CharField(max_length = 50, null=True)
    maktabi = models.CharField(max_length=50, null=True)
    tel_raqam = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return self.full_name

    