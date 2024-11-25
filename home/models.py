
from django.db import models 
from users.models import Teacher
# specifying choices 

class Category(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name
    
  
# Create your models here.
class Degrees(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
class Duration(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=150)
    degree = models.ForeignKey(Degrees, on_delete=models.SET_NULL, null=True)
    teacher = models.OneToOneField(Teacher, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    duration = models.ForeignKey(Duration, on_delete=models.SET_NULL, null=True)
    empty_seats = models.IntegerField(null=True)
    description = models.TextField(max_length=3000, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
class News(models.Model):
    title = models.CharField(max_length=150)
    added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    url= models.URLField()
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        ordering = ['-added']
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url