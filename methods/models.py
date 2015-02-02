
from django.db import models

class DiseaseModel(models.Model):
    taxonomic_id = models.TextField(
        help_text="The NCBI ID associated with this organism's species",
    )
    taxonomic_name = models.TextField(
        help_text="Taxon name for the organism under study.",
    )

    TISSUE_CULTURE = "tc"
    BIOPSY = "by"
    POST_MORTEM = "pm"
    CULTURE_CHOICES = (
        (TISSUE_CULTURE, "Tissue Culture"),
        (BIOPSY, "Biopsy"),
        (POST_MORTEM, "Post-Mortem"),
    )

    culture_type = models.CharField(
        max_length=2,
        choices=CULTURE_CHOICES,
        help_text="The source of the biological sample.",
    )
    genetics = models.TextField(
        help_text="A description of the controlled genetics of the organism (i.e. P53-/-).",
    )
    anatomy = models.TextField(
        null=True,
        blank=True,
        help_text="A description of the anatomical source of the sample, if relevant.",
    )
    description = models.TextField(
        help_text="A general description of the model organism.",
    )

class Citation(models.Model):
    string = models.TextField(
        help_text="A human readable form for the citation: (i.e. Author N, et al. (year)"
        "Title. <i>Journal</i> <b>Issue</b>, page-page",
    )
    pubmed_id = models.TextField(
        help_text="The Pubmed ID associated with this citation",
    )
    doi = models.TextField(
        help_text="The DOI reference associated with this citation",
    )

class Method(models.Model):
    disease_model = models.ForeignKey(
        DiseaseModel,
        help_text="The model organism used in this study.",
    )
    citation = models.ForeignKey(
        Citation,
        blank=True,
        null=True,
        help_text="The citation for this source of information.",
    )
