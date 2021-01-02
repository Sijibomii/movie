from .models import Review
from rest_framework import serializers

class reviewSerializer(serializers.ModelSerializer):
  username=serializers.CharField(source='user.name', read_only=True)
  class Meta:
    model = Review
    fields = ['username','comment', 'date_added', 'star_rating','user', 'movie']