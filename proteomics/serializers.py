
from proteomics import models

from rest_framework import serializers

# Serializers define the API representation.
class PeptideMethodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PeptideMethod
        fields = ()

class MSMethodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MSMethod
        fields = (
            "protocol_type",
            "enrichment",
            "validated_spectra",
            "cptac_id",
        )

class PeptideDataSetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PeptideDataSet
        fields = ("method", "description",)

class PeptideSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Peptide
        fields = ("data_set", "sequence", "protein", "phosphosite_plus_id",)

class ProteinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Protein
        fields = ("uniprot_id",)
