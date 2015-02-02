
from methods import models

from rest_framework import serializers

# Serializers define the API representation.
class DiseaseModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.DiseaseModel

class CitationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Citation

class MethodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Method
