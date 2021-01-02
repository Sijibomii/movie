from django.db import models
from movies.models import Movie
from auditorums.models import Auditoruim
# Create your models here.
class Screening(models.Model):
  screening_date=models.DateField()
  venue= models.ForeignKey(Auditoruim ,on_delete=models.CASCADE)
  time=models.TimeField()
  movie=models.ForeignKey(Movie,on_delete=models.CASCADE)

  def __str__(self):
    return self.movie.title