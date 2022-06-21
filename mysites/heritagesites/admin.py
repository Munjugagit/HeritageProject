from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin
from .models import Historicalsite, Sub_counties
from django.contrib.gis import admin


# Register your models here.
class HistoricalsiteAdmin(LeafletGeoAdmin):
    # pass
    list_display = ('Name', 'Location')


class Sub_countiesAdmin(LeafletGeoAdmin):
    # pass
    list_display = ('adm2_en', 'adm2_pcode')


admin.site.register(Historicalsite, HistoricalsiteAdmin)
admin.site.register(Sub_counties, Sub_countiesAdmin)
