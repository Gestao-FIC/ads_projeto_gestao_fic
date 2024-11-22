from django.urls import path
from sgset.views.SGSETView import SGSETView

urlpatterns = [
    path('', SGSETView.as_view(), name='scrape')
]
