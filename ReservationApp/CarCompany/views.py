from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CarCompany
from .serializer import CarCompanySerializer
# Create your views here.

class SearchForCarCompanies(APIView):
    def get(self , request , word):
        name_search = CarCompanySerializer(CarCompany.objects.filter(name__icontains=word) , many=True, context={"request": request})
        city_search = CarCompanySerializer(CarCompany.objects.filter(city__icontains=word) , many=True, context={"request": request})
        country_search = CarCompanySerializer(CarCompany.objects.filter(country__icontains=word) , many=True, context={"request": request})
        return Response({'name_search': name_search.data, 'city_search': city_search.data, 'country_search': country_search.data} , status=status.HTTP_200_OK)