from django.urls import path
from ..views.course_class_view import CourseClassModelDetail, CourseClassModelList

urlpatterns = [
    path('course-classes/', CourseClassModelList.as_view(), name='course-class-list'),
    path('course-classes/<str:pk>/', CourseClassModelDetail.as_view(), name='course-class-detail'),
]
