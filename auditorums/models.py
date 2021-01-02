from django.db import models

# Create your models here.
class Auditoruim(models.Model):
  name= models.CharField(max_length=255)
  no_of_seats=models.IntegerField()
  def __str__(self):
    return self.name