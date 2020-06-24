import uuid
from django.db import models
from django.urls import reverse

class Areas(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    name = models.CharField(max_length=200)

    description = models.CharField(max_length=1000, default='.')


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('area_detail', kwargs={'pk': str(self.pk)})
