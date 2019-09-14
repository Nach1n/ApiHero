from django.shortcuts import render
from hero.models import SuperHeroe, Publisher
from hero.serializers import SuperHeroeSerializer, PublisherSerializer
from rest_framework import generics

class SuperHeroeList(generics.ListCreateAPIView):
    queryset = SuperHeroe.objects.all()
    serializer_class = SuperHeroeSerializer

class SuperHeroeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SuperHeroe.objects.all()
    serializer_class = SuperHeroeSerializer

class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class PublisherList(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


