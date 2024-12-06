from django.urls import path
from sgset.views.InstructorView import InstructorListView, InstructorDetailView  # Import both views

urlpatterns = [
    path('', InstructorListView.as_view(), name='Instructor-list'),
    path('<uuid:Instructor_id>/', InstructorDetailView.as_view(), name='Instructor-detail'),
]