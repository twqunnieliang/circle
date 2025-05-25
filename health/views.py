from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

class HealthCheckView(APIView):
    @extend_schema(
        summary="Health Check",
        description="Returns status ok if the service is up.",
        responses={200: {'type': 'object', 'properties': {'status': {'type': 'string'}}}}
    )
    def get(self, request):
        return Response({"status": "ok"}, status=status.HTTP_200_OK)
