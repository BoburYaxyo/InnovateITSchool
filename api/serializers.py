from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from home.models import Subject, Category, Degrees,Duration, News, Post
from users.models import Teacher
# from blog.models import Blog,BCategory, Post
# from books.models import Cart, Order, OrderItem
# from books.models import Book, Review, Sizes, Tags, Category
# from blog import models


class DegreeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Degrees
        fields = "__all__"


class CatSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class DurSerializer(ModelSerializer):

    class Meta:
        model = Duration
        fields = '__all__'


class NewsSerializer(ModelSerializer):

    class Meta:
        model = News
        fields = '__all__'


class TeacherSerializer(ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'


# class BookSerializer(ModelSerializer):
#     reviews = ReviewSerializer(many=True, read_only=True)
#     size = SizeSerializer(many=True, read_only=True)
#     color = ColorSerializer(read_only=True)
#     tags = TagSerializer(read_only=True)
#     category = CategorySerializer(read_only=True)
#     brands = BrandSerializer(read_only=True)
#     user = serializers.StringRelatedField()

#     class Meta:
#         model = Book
#         fields = "__all__"

class SubSerializer(ModelSerializer):
    teacher = TeacherSerializer(read_only=True)
    duration = DurSerializer(read_only=True)
    categories = CatSerializer(read_only=True)
    classes = DegreeSerializer(read_only=True)
    class Meta:
        model = Subject
        fields = "__all__"







        
# class OrderSerializer(ModelSerializer):

#     class Meta:
#         model = Order
#         fields = "__all__"
        
# class OrderItemSerializer(ModelSerializer):
#     order = OrderSerializer(read_only=True)
    
#     class Meta:
#         model = OrderItem
#         fields = "__all__"

# class PostSerializer(ModelSerializer):

#     class Meta:
#         model = Post
#         fields = "__all__"

# class BcategorySerializer(ModelSerializer):
    
#     class Meta:
#         model = BCategory
#         fields = "__all__"
        

# class BlogSerializer(ModelSerializer):
#     posts = PostSerializer(many=True, read_only=True)
#     bcategory = BcategorySerializer(read_only=True)
#     posted_by = serializers.StringRelatedField()

#     class Meta:
#         model = Blog
#         fields = "__all__"

