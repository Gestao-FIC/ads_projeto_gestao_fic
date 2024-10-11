from django.urls import path
from sgset.views.AuthView import AuthView

urlpatterns = [
    path('', AuthView.as_view(), name='login'),
]
