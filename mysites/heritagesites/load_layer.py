from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import Sub_counties

sub_counties_mapping = {
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'adm2_en': 'ADM2_EN',
    'adm2_pcode': 'ADM2_PCODE',
    'adm1_en': 'ADM1_EN',
    'adm1_pcode': 'ADM1_PCODE',
    'adm0_en': 'ADM0_EN',
    'adm0_pcode': 'ADM0_PCODE',
    'geom': 'MULTIPOLYGON',
}

subcounty_shp = Path(__file__).resolve().parent / 'Data' / 'sub_counties.shp'

def run(verbose=True):
    lm = LayerMapping(Sub_counties, subcounty_shp, sub_counties_mapping, transform= False, encoding= 'iso-8859-1' )
    lm.save(strict=True, verbose=verbose)