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
    
    