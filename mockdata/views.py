from django.shortcuts import render

# apps/circle/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MockAPISerializer
from .models import MockAPI
from drf_spectacular.utils import extend_schema, OpenApiParameter
import json

class MockDataCreateView(APIView):
    
    # POST mock data
    @extend_schema(
        request=MockAPISerializer,
        responses={201: MockAPISerializer},
        summary="Ceate a new mock data"
    )
    def post(self, request):
        request.data['mock_data'] = json.dumps(request.data['mock_data'])
        serializer = MockAPISerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    # GET mock data
    @extend_schema(
        parameters=[
            OpenApiParameter(name='project_name', type=str, required=False, description='filter by project_name')
        ],
        responses=MockAPISerializer(many=True),
        summary="Query mock data by project_name"
    )
    def get(self, request):
        project_name = request.query_params.get('project_name')

        queryset = MockAPI.objects.all()

        if project_name:
            queryset = queryset.filter(project_name=project_name)
        else:
            return Response("loss project_name", status=status.HTTP_400_BAD_REQUEST)


        serializer = MockAPISerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

