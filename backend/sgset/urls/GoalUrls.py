from django.urls import path
from sgset.views.GoalView import GoalView

urlpatterns = [
    path('', GoalView.as_view(), name='goal'),
]
