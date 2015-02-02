
from django_rest_omics.urls import router

from proteomics import viewsets

router.register(r'proteins', viewsets.ProteinViewSet)
router.register(r'peptides', viewsets.PeptideViewSet)
