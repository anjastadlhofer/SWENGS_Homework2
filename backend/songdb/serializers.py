from rest_framework import serializers
from .models import Country, Song, Person


class CountryOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']


class PersonOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

    #def get_name(self, obj):
        #return ' '.join(filter(None, (obj.first_name, obj.last_name)))


class SongFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


class SongListSerializer(serializers.ModelSerializer):
    country_name = serializers.SerializerMethodField()

    class Meta:
        model = Song
        fields = ['id', 'title', 'genre', 'release_date', 'story', 'selled', 'country_name', 'band',
                  'singers']

    def get_country_name(self, obj):
        return obj.country.name if obj.country else ''

