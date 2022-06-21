# We have to import the packages from gis model
from django.contrib.gis.db import models


# Create your models here.
class Historicalsite(models.Model):
    # Regular Django fields corresponding to the attributes
    Name = models.TextField()
    Location = models.PointField(srid=4326)
    Image = models.ImageField()
    PlotNo = models.CharField(max_length=20)
    Area = models.FloatField()
    Dev_plotno = models.IntegerField()
    Section = models.CharField(max_length=10)

    # Returns the string representation of the model.
    def __str__(self):
        return self.Name

    class Meta:
        verbose_name_plural = "Historical Sites"


class Sub_counties(models.Model):
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    adm2_en = models.CharField(max_length=50)
    adm2_pcode = models.CharField(max_length=50)
    adm1_en = models.CharField(max_length=50)
    adm1_pcode = models.CharField(max_length=50)
    adm0_en = models.CharField(max_length=50)
    adm0_pcode = models.CharField(max_length=50)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.adm2_en

    class Meta:
        verbose_name_plural = "Sub_counties"
