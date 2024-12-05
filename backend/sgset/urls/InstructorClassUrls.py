from django.urls import path
from sgset.views.InstructorClassView import InstructorClassListView, InstructorClassDetailView  # Import both views

urlpatterns = [
    path('', InstructorClassListView.as_view(), name='InstructorClass-list'),
    path('<uuid:InstructorClass_id>/', InstructorClassDetailView.as_view(), name='InstructorClass-detail'),
]