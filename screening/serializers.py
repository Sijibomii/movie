from .models import Screening
from rest_framework import serializers

class screeningSerializer(serializers.ModelSerializer):
  venue_name=serializers.CharField(source='venue.name', read_only=True)
  movie_name=serializers.CharField(source='movie.title', read_only=True)
  class Meta:
    model = Screening
    fields = fields = ['movie_name','venue_name','time', 'screening_date','venue','movie']
  
       