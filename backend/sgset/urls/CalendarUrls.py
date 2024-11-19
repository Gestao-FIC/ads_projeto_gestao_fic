from django.urls import path
from ..views import CalendarView

urlpatterns = [
    path('calendar/', CalendarView.as_view(), name='calendar_list_create'),
    path('calendar/<uuid:event_id>/', CalendarView.as_view(), name='calendar_detail'),
]
