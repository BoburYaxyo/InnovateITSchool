from django.shortcuts import render, redirect
from .models import Subject, Category, Degrees, News
from users.models import Teacher, Student
from django.db.models import Q
from .utils import paginateProducts
from .models import Post
# Create your views here.
def home(request):
    subjects = Subject.objects.all()
    teachers= Teacher.objects.all()
    sub_count = subjects.count()
    te_count =teachers.count()
    degrees = Degrees.objects.all()
    de_count = degrees.count()
    if request.method == 'POST': 
        name = request.POST.get('name') 
        email = request.POST.get('email') 
        subject = request.POST.get('subject')
        comment = request.POST.get('comment')
 
        # Save to database 
        if name and email: 
            contact = Post(name=name, email=email, subject=subject, comment=comment) 
            contact.save() 
            return redirect('contact') 
    
    if request.method == 'POST': 
        full_name = request.POST.get('full_name') 
        tel_raqami = request.POST.get('tel_raqami') 
        maktabi = request.POST.get('maktabi')
        sinfi = request.POST.get('sinfi')
 
        # Save to database 
        if full_name and tel_raqami: 
            user = Student(full_name=full_name, tel_raqam=tel_raqami, maktabi=maktabi, sinfi=sinfi) 
            user.save() 
            return redirect('home') 
    posts = Post.objects.all()
    context={
        'subjects':subjects,
        'sub_count':sub_count,
        'te_count':te_count,
        'de_count':de_count,
        'posts':posts,
        'teachers': teachers,
    }
    return render(request, 'home.html', context)

def about(request):

    return render(request, 'about.html')

def news(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    news = News.objects.filter(
        Q(title__icontains=q) 
    )
    context = {
        'news':news,
    
    }
    return render(request, 'news.html', context)

def course(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    subject = Subject.objects.filter(
        Q(category__name__icontains=q) |
        Q(name__icontains=q) |
        Q(degree__name__icontains=q) |
        Q(teacher__name__icontains=q) 
    )
    sub_count = subject.count()
    custom_range, subject = paginateProducts(request, subject, 3)
    context = {
        'subject':subject,
        'sub_count':sub_count,
        'custom_range':custom_range,
        }
    return render(request, 'course.html', context)

def course_detail(request, pk):
    subjects = Subject.objects.all()
    subject = Subject.objects.get(pk=pk)
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    categories = Category.objects.filter(name__icontains=q)


    context = {
        'subject':subject,
        'subjectss':subjects,
        'categories':categories,
        }
    return render(request, 'detail.html', context)

def feature(request):

    return render(request, 'feature.html')

def contact(request):
    
    if request.method == 'POST': 
        name = request.POST.get('name') 
        email = request.POST.get('email') 
        subject = request.POST.get('subject')
        comment = request.POST.get('comment')
 
        # Save to database 
        if name and email: 
            contact = Post(name=name, email=email, subject=subject, comment=comment) 
            contact.save() 
            return redirect('contact') 
    
    context = {}
    return render(request, 'contact.html', context)

def team(request):

    return render(request, 'team.html')

def testimonial(request):

    return render(request, 'testimonial.html')

