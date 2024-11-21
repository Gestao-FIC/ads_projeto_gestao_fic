from django.urls import path
from sgset.views.CalendarView import EventListView, EventDetailView

urlpatterns = [
    path('', EventListView.as_view(), name='calendar_list'),  # GET para listar, POST para criar
    path('<uuid:pk>/', EventDetailView.as_view(), name='calendar_detail'),  # GET, PUT, DELETE para item específico
]
