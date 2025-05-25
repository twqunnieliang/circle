# apps/circle/urls.py

from django.urls import path
from .views import MockDataCreateView

urlpatterns = [
    path('mock-data/', MockDataCreateView.as_view(), name='mock-data-create'),
]
