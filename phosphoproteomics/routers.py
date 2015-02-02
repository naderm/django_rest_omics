
from django_rest_omics.urls import router

from phosphoproteomics import viewsets

router.register(r'phopshopeptides', viewsets.PhosphopeptideViewSet)
