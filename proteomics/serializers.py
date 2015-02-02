
from proteomics import models

from rest_framework import serializers

# Serializers define the API representation.
class PeptideSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Peptide
        fields = ()

class ProteinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Protein
        fields = ()
