from rest_framework import serializers
  
# import model from models.py
from .models import GeeksModel
  
# Create a model serializer 
class GeeksSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = GeeksModel
        fields = ('url', 'id', 'title', 'description')