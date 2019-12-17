from django.contrib import admin
from .models import *


class SongAdmin(admin.ModelAdmin):
    list_filter = ('singers__last_name',)


class PersonAdmin(admin.ModelAdmin): pass


class CountryAdmin(admin.ModelAdmin): pass


admin.site.register(Song, SongAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Country, CountryAdmin)
