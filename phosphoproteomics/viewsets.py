
from rest_framework import viewsets

from phosphoproteomics import models, serializers

# ViewSets define the view behavior.
class PhosphopeptideViewSet(viewsets.ModelViewSet):
    queryset = models.Phosphopeptide.objects.all()
    serializer_class = serializers.PhosphopeptideSerializer
