from django.urls import path
from sgset.views.CalendarView import CalendarView

urlpatterns = [
    path('', CalendarView.as_view(), name='calendar_list_create'),
    path('<uuid:event_id>/', CalendarView.as_view(), name='calendar_detail'),
]