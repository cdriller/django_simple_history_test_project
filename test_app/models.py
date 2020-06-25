from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    history = HistoricalRecords()