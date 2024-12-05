from django.urls import path
from ..views.auth_view import AuthView

urlpatterns = [
    path('', AuthView.as_view(), name='login'),
]
