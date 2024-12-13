from django.urls import path
from .views import log_request

urlpatterns = [
    path('log/', log_request, name='log_request'),
]