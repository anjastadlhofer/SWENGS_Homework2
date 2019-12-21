from django.shortcuts import render

from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from songdb.models import Country, Song, Person
from songdb.serializers import CountryOptionSerializer, SongFormSerializer, PersonOptionSerializer


#@swagger_auto_schema(method='GET', responses={200: CountryOptionSerializer(many=True)})
@api_view(['GET'])
def country_option_list(request):
    countries = Country.objects.all()
    serializer = CountryOptionSerializer(countries, many=True)
    return Response(serializer.data)


#@swagger_auto_schema(method='GET', responses={200: PersonOptionSerializer(many=True)})
@api_view(['GET'])
def person_list(request):
    persons = Person.objects.all()
    serializer = PersonOptionSerializer(persons, many=True)
    return Response(serializer.data)


#@swagger_auto_schema(method='GET', responses={200: SongListSerializer(many=True)})
@api_view(['GET'])
def songs_list(request):
    countries = Song.objects.all()
    serializer = SongFormSerializer(countries, many=True)
    return Response(serializer.data)

##########################################################

#@swagger_auto_schema(method='POST', request_body=SongFormSerializer, responses={200: SongFormSerializer()})
@api_view(['POST'])
def person_form_create(request):
    #data = JSONParser().parse(request)
    serializer = PersonOptionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


#@swagger_auto_schema(method='PUT', request_body=SongFormSerializer, responses={200: SongFormSerializer()})
@api_view(['PUT'])
def person_form_update(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response({'error': 'Person does not exist.'}, status=404)

    data = JSONParser().parse(request)
    serializer = PersonOptionSerializer(person, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


#@swagger_auto_schema(method='GET', responses={200: SongFormSerializer()})
@api_view(['GET'])
def person_form_get(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response({'error': 'Person does not exist.'}, status=404)

    serializer = PersonOptionSerializer(person)
    return Response(serializer.data)


@api_view(['DELETE'])
def person_delete(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response({'error': 'Person does not exist.'}, status=404)
    person.delete()
    return Response(status=204)


##########################################################


#@swagger_auto_schema(method='POST', request_body=SongFormSerializer, responses={200: SongFormSerializer()})
@api_view(['POST'])
def song_form_create(request):
    serializer = SongFormSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


#@swagger_auto_schema(method='PUT', request_body=SongFormSerializer, responses={200: SongFormSerializer()})
@api_view(['PUT'])
def song_form_update(request, pk):
    try:
        song = Song.objects.get(pk=pk)
    except Song.DoesNotExist:
        return Response({'error': 'Song does not exist.'}, status=404)

    data = JSONParser().parse(request)
    serializer = SongFormSerializer(song, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


#@swagger_auto_schema(method='GET', responses={200: SongFormSerializer()})
@api_view(['GET'])
def song_form_get(request, pk):
    try:
        song = Song.objects.get(pk=pk)
    except Song.DoesNotExist:
        return Response({'error': 'Song does not exist.'}, status=404)

    serializer = SongFormSerializer(song)
    return Response(serializer.data)


@api_view(['DELETE'])
def song_delete(request, pk):
    try:
        song = Song.objects.get(pk=pk)
    except Country.DoesNotExist:
        return Response({'error': 'Song does not exist.'}, status=404)
    song.delete()
    return Response(status=204)

