from django.urls import path

from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('feature/', views.feature, name='feature'),
    path('detail/<int:pk>/', views.course_detail, name='detail'),
    path('course/', views.course, name='course'),
    path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('news/', views.news, name='news'),
]