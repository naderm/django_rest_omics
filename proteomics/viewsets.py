
from rest_framework import viewsets

from proteomics import models, serializers

# ViewSets define the view behavior.
class PeptideViewSet(viewsets.ModelViewSet):
    queryset = models.Peptide.objects.all()
    serializer_class = serializers.PeptideSerializer

class ProteinViewSet(viewsets.ModelViewSet):
    queryset = models.Protein.objects.all()
    serializer_class = serializers.ProteinSerializer
