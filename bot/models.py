from django.db import models
import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Quote(models.Model):
    author = models.CharField(max_length=200)
    quote_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.quote_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


