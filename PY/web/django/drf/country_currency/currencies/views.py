from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Country
from .serializers import CountrySerializer


# Create your views here.

@api_view(['GET', 'POST'])
def country(request):
    if request.method == 'GET':
        snippets = Country.objects.all()
        serializers = CountrySerializer(snippets, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
