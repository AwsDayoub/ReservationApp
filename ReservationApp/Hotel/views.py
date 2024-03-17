from django.shortcuts import render
from django.db.models import F
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Hotel
from .serializer import HotelSerializer
from drf_spectacular.utils import extend_schema
# Create your views here.


class SearchForHotels(APIView):
    
    def get(self , request , word):
        name_search = HotelSerializer(Hotel.objects.filter(name__icontains=word) , many=True, context={"request": request})
        city_search = HotelSerializer(Hotel.objects.filter(city__icontains=word) , many=True, context={"request": request})
        country_search = HotelSerializer(Hotel.objects.filter(country__icontains=word) , many=True, context={"request": request})
        return Response({'name_search': name_search.data, 'city_search': city_search.data, 'country_search': country_search.data} , status=status.HTTP_200_OK)
    


class ShowHotels(APIView):
    def get(self , request):
        hotels = Hotel.objects.annotate(rate=F('sum_of_rates') / F('number_of_rates')).order_by('rate', '-date_created')
        serializer = HotelSerializer(hotels , many = True , context={"request": request})
        return Response(serializer.data , status=status.HTTP_200_OK)