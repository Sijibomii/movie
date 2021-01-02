from django.db import models
from accounts.models import UserAccount
from auditorums.models import Auditoruim
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Seat(models.Model):
  class seatType(models.TextChoices):
    BOOKED='BOOKED'
    ASSIGNED='ASSIGNED'
    EMPTY='EMPTY'
  user=models.ForeignKey(UserAccount, on_delete=models.CASCADE,blank=True, null=True)
  aud=models.ForeignKey(Auditoruim, on_delete=models.CASCADE)
  status=models.CharField(max_length=50, choices=seatType.choices, default=seatType.EMPTY)

  def __str__(self):
    return self.aud.name
@receiver(post_save, sender=Auditoruim)
def create_seats(sender, instance, created, **kwargs):
  if created:
    for x in range(instance.no_of_seats):
      Seat.objects.create(aud=instance)
    print('seats created!!!!!!!!!!')