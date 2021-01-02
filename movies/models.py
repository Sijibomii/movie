from django.db import models
from datetime import datetime
from django.utils.timezone import now
# Create your models here.
class Movie(models.Model):
  class ratingType(models.TextChoices):
    RATED_PG='PG'
    RATED_18='18+'
    RATED_16='16+'
    RATED_21='21+'
    RATED_13='13+'
  title=models.CharField(max_length=150)
  duraration=models.CharField(max_length=150)
  trailer=models.FileField(upload_to='videos/%Y/%m/%d/', blank=True, null=True)
  images=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
  rated=models.CharField(max_length=50, choices=ratingType.choices, default=ratingType.RATED_PG)
  genre=models.CharField(max_length=100)
  director=models.CharField(max_length=250)
  cast=models.TextField()
  description=models.TextField()
  release_date=models.DateField(default=now, blank=True)

  def __str__(self):
    return self.title