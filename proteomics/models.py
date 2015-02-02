
from django.db import models

from methods.models import Method

### Methods
class PeptideMethod(Method):
    pass

class MSMethod(PeptideMethod):
    protocol_type = models.TextField(
        help_text="The general type of protocol used (i.e. LC-MS/MS)",
    )
    enrichment = models.TextField(
        null=True,
        blank=True,
        help_text="The type of enrichment used before data collection (i.e. Fe-IMAC).",
    )
    validated_spectra = models.BooleanField(
        default=False,
        help_text="Indicates if the scientists performing the method manually validated "
        "their results for correctness",
    )
    cptac_id = models.TextField(
        null=True,
        blank=True,
        help_text="The CPTAC ID associated with this data set.",
    )

#### Data Sets
class PeptideDataSet(models.Model):
    method = models.ForeignKey(
        PeptideMethod,
        relatedname="peptide_dataset",
        help_text="The method used to generate this data set.",
    )
    description = models.TextField(
        help_text="Any extra information associated with this data set.",
    )

class PeptideDataSource(models.Model):
    data_set = models.ForeignKey(
        PeptideDataSet,
        related_name="datasource",
        help_text="The data set this source is associated with.",
    )
    url = models.TextField(
        help_text="The URL pointing to this data set.",
    )
    description = models.TextField(
        help_text="A description of this particular data source.",
    )

### Individual Peptides / Proteins
class Protein(models.Model):
    # transcript =
    uniprot_id = models.TextField(
        help_text="The ID of this protein in the UniProt Database",
    )

class Peptide(models.Model):
    data_set = models.ForeignKey(
        PeptideDataSet,
        related_name="peptide",
        help_text="The data set this peptide read is associated with.",
    )
    sequence = models.TextField(
        help_text="Sequence of the peptide read.",
    )
    # XXX: ManyToMany field for ambiguous assignments?
    protein = models.ManyToManyField(
        Protein,
        related_name="peptide",
        help_text="Protein this peptide was assigned to.",
    )
    phosphosite_plus_id = models.TextField(
        null=True,
        blank=True,
        help_text="The ID of this site in the PhosphoSitePlus Database.",
    )
