from django.urls import path
from sgset.views.goals_view import GoalListView, GoalDetailView  # Import both views

urlpatterns = [
    path('', GoalListView.as_view(), name='goal-list'),
    path('<uuid:goal_id>/', GoalDetailView.as_view(), name='goal-detail'),
]