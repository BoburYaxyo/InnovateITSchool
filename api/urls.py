from django.urls import path, include
from .views import SubjectVS,NewsVS,TeacherVS,PostVS
# from .views import BlogVS, OrderItemVS, PostVS, ReviewVS, BookVS, OrderVS
# from django.utils.translation import gettext_lazy as _
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('subjectvs', SubjectVS, basename='subjectvs')
router.register('news', NewsVS, basename='newsvs')
router.register('teachervs', TeacherVS, basename='teachervs')
router.register('postvs', PostVS, basename='postvs')
# router.register('reviewvs', ReviewVS, basename='reviewvs')
# router.register('itemvs', OrderItemVS, basename='itemvs')


urlpatterns = [
    path('', include(router.urls)),
]
