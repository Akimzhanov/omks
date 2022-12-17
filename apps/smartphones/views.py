from django.shortcuts import render
from .models import Brand, Smartphone
from .serializers import (BrandSerializer, SmartphoneListSerializer, SmartphoneSerializer)
from rest_framework.generics import (ListAPIView, ListCreateAPIView, CreateAPIView, UpdateAPIView,
                                     RetrieveAPIView, RetrieveUpdateDestroyAPIView)


class SmartphoneListAPIView(ListAPIView):
    queryset = Smartphone.objects.all()
    serializer_class = SmartphoneListSerializer
    
    
class SmartphoneAPIView(RetrieveAPIView):
    queryset = Smartphone.objects.all()
    serializer_class = SmartphoneSerializer
    lookup_field = 'slug'


class SmartphoneCreateAPIView(CreateAPIView):
    queryset = Smartphone.objects.all()
    serializer_class = SmartphoneSerializer


class SmartphoneUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Smartphone.objects.all()
    serializer_class = SmartphoneSerializer
    lookup_field = 'slug'


class BrandListAPIView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandAPIView(RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field = 'slug'



