# apps/circle/models.py

import uuid
from django.db import models

class MockAPI(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project_name = models.CharField(max_length=48)
    api_name = models.CharField(max_length=256)
    mock_data = models.CharField(null=True, blank=True,max_length=1024)
    create_user = models.CharField(max_length=16)
    create_date = models.DateField()
    description = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        db_table = 'mock_api'
