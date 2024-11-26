# from blog.models import Blog, Post
# from books.models import Cart, Order, OrderItem
# from books.models import Book, Review
# # from rest_framework.response import Response
# # from rest_framework import status\
from rest_framework import viewsets
from home.models import Subject, News, Post
from users.models import Teacher

# from users.models import Profile
# # from rest_framework.views import APIView
# from .serializers import BlogSerializer, OrderItemSerializer, OrderSerializer, PostSerializer,BookSerializer, ReviewSerializer
from .serializers import SubSerializer, NewsSerializer, TeacherSerializer, PostSerializer
# from django.utils.translation import gettext_lazy as _
# from rest_framework import generics, mixins

# class ReviewVS(viewsets.ModelViewSet):

#     serializer_class = ReviewSerializer
#     queryset = Review.objects.all()



class SubjectVS(viewsets.ModelViewSet):

    serializer_class = SubSerializer
    queryset = Subject.objects.all()


class NewsVS(viewsets.ModelViewSet):

    serializer_class = NewsSerializer
    queryset = News.objects.all()

# class OrderItemVS(viewsets.ModelViewSet):

#     serializer_class = OrderItemSerializer
#     queryset = OrderItem.objects.all()

class TeacherVS(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    
class PostVS(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

