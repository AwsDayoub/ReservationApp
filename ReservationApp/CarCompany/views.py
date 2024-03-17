from django.shortcuts import render
from django.db.models import Q , F
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CarCompany
from .serializer import CarCompanySerializer
from .paginations import CarCompanyListPagination
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from .permissions import IsManager
from rest_framework import generics
# Create your views here.


class SearchForCarCompanies(generics.ListAPIView):
    serializer_class = CarCompanySerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get_queryset(self):
        word = self.kwargs.get('word', '')
        queryset = CarCompany.objects.filter(
            Q(name__icontains=word) |
            Q(city__icontains=word) |
            Q(country__icontains=word)
        )
        return queryset


class ShowCarCompanies(generics.ListAPIView):
    queryset = CarCompany.objects.annotate(rate=F('sum_of_rates') / F('number_of_rates')).order_by('rate', '-date_created')
    serializer_class = CarCompanySerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    pagination_class = CarCompanyListPagination