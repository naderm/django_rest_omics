
from proteomics import models

from rest_framework import serializers

# Serializers define the API representation.
class PeptideMethodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PeptideMethod

class MSMethodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MSMethod

class PeptideDataSetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PeptideDataSet

class PeptideSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Peptide

class ProteinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Protein
