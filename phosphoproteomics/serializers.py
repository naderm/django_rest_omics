
from rest_framework import serializers

from phosphoproteomics import models

class PhosphopeptideSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Phosphopeptide
        fields = ()
