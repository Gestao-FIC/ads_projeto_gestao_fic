from django.urls import path
from ..views.course_view import CourseModelList, CourseModelDetail

urlpatterns = [
    path('courses/', CourseModelList.as_view(), name='course_list'),
    path('courses/<uuid:pk>/', CourseModelDetail.as_view(), name='course_detail'),
]
