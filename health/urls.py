from django.urls import path
from .views import HealthCheckView

urlpatterns = [
    path('self/health-check', HealthCheckView.as_view(), name='health-check'),
]
