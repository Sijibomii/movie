from .models import Movie
from rest_framework import serializers

class movieSerializer(serializers.ModelSerializer):
  class Meta:
    model = Movie
    fields = '__all__'
  
      