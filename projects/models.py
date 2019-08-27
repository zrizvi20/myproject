from django.db import models
from django.conf import settings
from users.models import *

from django_countries.fields import CountryField


class ProjectTypes(models.Model):
    project_type_id = models.AutoField(primary_key=True)
    COMMERCIAL = 'commercial'
    RESIDENTIAL = 'residential'
    project_types = (
        (COMMERCIAL, 'Commercial'),
        (RESIDENTIAL, 'Residential'),
        )
    project_type_name = models.CharField(
        max_length=150,
        choices = project_types,
        default = RESIDENTIAL,
        verbose_name = 'Project type')
    project_type_desc = models.CharField(max_length=150, blank=True, verbose_name = 'Project Type Description')

    def __str__(self):
        return self.project_type_name

    class Meta:
        verbose_name = 'Project Types'
        verbose_name_plural = 'Project Types'


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=150, verbose_name = 'Project Name')
    project_desc_1 = models.CharField(max_length=150, verbose_name = 'Project Description')
    project_desc_2 = models.CharField(max_length=150, blank=True, verbose_name = 'Project Description')
    project_desc_3 = models.CharField(max_length=150, blank=True, verbose_name = 'Project Description')
    site_address_1 = models.CharField(max_length=150, verbose_name = 'Site Address')
    site_address_2 = models.CharField(max_length=150, blank=True, verbose_name = 'Site Address')
    site_address_3 = models.CharField(max_length=150, blank=True, verbose_name = 'Site Address')
    city = models.ForeignKey('location.City', on_delete=models.CASCADE, verbose_name = 'City')
    region = models.ForeignKey('location.Region', on_delete=models.CASCADE, verbose_name = 'Region')
    country = models.ForeignKey('location.Country', on_delete=models.CASCADE, verbose_name = 'Country')
    site_postal_code = models.CharField(max_length=150, verbose_name = 'Site Postal Code')
    site_po_box_no = models.CharField(max_length=150, verbose_name = 'Site P.O. Box Number')
    plot_size = models.DecimalField(max_digits=5, decimal_places=2, verbose_name = 'Plot Size')
    plot_area_units = models.ForeignKey('units.PlotAreaUnits', on_delete=models.CASCADE, verbose_name = 'Plot Area Units')
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name = 'Client')
    project_type = models.ForeignKey(ProjectTypes, on_delete=models.CASCADE, verbose_name = 'Project Type')
    no_of_floors = models.IntegerField(verbose_name = 'Number of Floors')
    total_covered_area = models.DecimalField(max_digits=5, decimal_places=2, verbose_name = 'Total Covered Area')
    covered_area_units = models.ForeignKey('units.CoveredAreaUnits', on_delete=models.CASCADE, verbose_name = 'Covered Area Unit')
    contractor = models.ForeignKey (User, on_delete = models.CASCADE, related_name='coprojects')
    supervisor = models.ForeignKey (User, on_delete = models.CASCADE, related_name='suprojects')
    client = models.ForeignKey (User, on_delete = models.CASCADE, related_name='clprojects')

    def __str__(self):
        return self.project_name
