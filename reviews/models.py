from django.db import models
from accounts.models import UserAccount
from datetime import datetime

from movies.models import Movie
# Create your models here.
class Review(models.Model):
  movie=models.ForeignKey(Movie, related_name='movie',null=True, on_delete=models.PROTECT)
  user=models.ForeignKey(UserAccount,related_name='user',null=True, on_delete=models.PROTECT)
  comment=models.TextField()
  date_added=models.DateTimeField(default=datetime.now())
  star_rating=models.IntegerField()

  def __str__(self):
      return self.user.name
  
