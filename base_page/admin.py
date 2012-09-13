"""
Admin classes for base_page related models
"""
from django.contrib.gis import admin
from base_page.models import Feedback
from base_page.models import CitySetting
from django.conf import settings
from modeltranslation.admin import TranslationAdmin
    
class CitySettingAdmin(TranslationAdmin, admin.OSMGeoAdmin):
    """
    The CitySettingAdmin handles the city/organization specific settings
    for the site.
    """
    list_display = ('city_name',
                    'title',
                    'blurb',
                    'provider',)
    
    default_lon = getattr(settings,
                          'ORGANIZATION_ADMIN_DEFAULT_MAP_SETTINGS',
                          {'default_lon': 0})['default_lon']
    default_lat = getattr(settings,
                          'ORGANIZATION_ADMIN_DEFAULT_MAP_SETTINGS',
                          {'default_lat': 0})['default_lat']
    default_zoom = getattr(settings,
                          'ORGANIZATION_ADMIN_DEFAULT_MAP_SETTINGS',
                          {'default_zoom': 4})['default_zoom']
   
admin.site.register(Feedback)
admin.site.register(CitySetting, CitySettingAdmin)
