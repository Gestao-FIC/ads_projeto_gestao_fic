from django.urls import path
from ..views.update_quorum_view import UpdateCourseClassQuorum

urlpatterns = [
    path('quorum/course-classes/<str:code>/update-quorum/', UpdateCourseClassQuorum.as_view(), name='update-course-class-quorum'),
]
