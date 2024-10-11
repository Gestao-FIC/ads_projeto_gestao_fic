from django.urls import path
from sgset.views.AuthView import AuthView

urlpatterns = [
    path('api/login/', AuthView.as_view(), name='login'),
]
