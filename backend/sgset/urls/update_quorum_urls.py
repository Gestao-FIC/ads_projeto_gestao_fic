from django.urls import path
from ..views.update_quorum import UpdateCourseClassQuorum

urlpatterns = [
    path('quorum/course-classes/<str:code>/update-quorum/', UpdateCourseClassQuorum.as_view(), name='update-course-class-quorum'),
]
