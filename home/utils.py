import json
from .models import *
from django.db.models import Sum
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
def paginateProducts(request, subjects, results):

    page = request.GET.get('page')
    paginator = Paginator(subjects, results)

    try:
        subjects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        subjects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        subjects = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, subjects