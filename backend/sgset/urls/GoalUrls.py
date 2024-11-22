from django.urls import path
from sgset.views.GoalView import GoalListView, GoalDetailView  # Import both views

urlpatterns = [
    path('', GoalListView.as_view(), name='goal-list'),
    path('<uuid:goal_id>/', GoalDetailView.as_view(), name='goal-detail'),
]