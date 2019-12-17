from django.shortcuts import render

from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from songdb.models import Country, Song, Person
from songdb.serializers import CountryOptionSerializer, SongListSerializer, SongFormSerializer, PersonOptionSerializer


@swagger_auto_schema(method='GET', responses={200: CountryOptionSerializer(many=True)})
@api_view(['GET'])
def country_option_list(request):
    countries = Country.objects.all()
    serializer = CountryOptionSerializer(countries, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='GET', responses={200: PersonOptionSerializer(many=True)})
@api_view(['GET'])
def person_option_list(request):
    persons = Person.objects.all()
    serializer = PersonOptionSerializer(persons, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='GET', responses={200: SongListSerializer(many=True)})
@api_view(['GET'])
def movies_list(request):
    countries = Song.objects.all()
    serializer = SongListSerializer(countries, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='POST', request_body=SongFormSerializer, responses={200: SongFormSerializer()})
@api_view(['POST'])
def movie_form_create(request):
    data = JSONParser().parse(request)
    serializer = SongFormSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@swagger_auto_schema(method='PUT', request_body=SongFormSerializer, responses={200: SongFormSerializer()})
@api_view(['PUT'])
def movie_form_update(request, pk):
    try:
        song = Song.objects.get(pk=pk)
    except Song.DoesNotExist:
        return Response({'error': 'Movie does not exist.'}, status=404)

    data = JSONParser().parse(request)
    serializer = SongFormSerializer(song, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@swagger_auto_schema(method='GET', responses={200: SongFormSerializer()})
@api_view(['GET'])
def movie_form_get(request, pk):
    try:
        song = Song.objects.get(pk=pk)
    except Song.DoesNotExist:
        return Response({'error': 'Movie does not exist.'}, status=404)

    serializer = SongFormSerializer(song)
    return Response(serializer.data)


@api_view(['DELETE'])
def movie_delete(request, pk):
    try:
        song = Song.objects.get(pk=pk)
    except Country.DoesNotExist:
        return Response({'error': 'Movie does not exist.'}, status=404)
    song.delete()
    return Response(status=204)

