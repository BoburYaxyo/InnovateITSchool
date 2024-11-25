from django.contrib import admin
from home.models import Subject,Degrees, Duration, Category, News
# # Register your models here.
admin.site.register(Subject)
admin.site.register(Degrees)
admin.site.register(Duration)
admin.site.register(Category)
admin.site.register(News)