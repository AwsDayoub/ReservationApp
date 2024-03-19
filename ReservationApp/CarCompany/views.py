from django.shortcuts import render , get_object_or_404
from django.db.models import Q , F , Prefetch
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CarCompany , CarCompanyImages , Car , CarImages , CarReservation , CarReservationIdImage , CarCompanyComments
from .serializer import CarCompanySerializer , CarCompanyWithImagesSerializer , CarWithCarImagesSerializer , CarReservationWithIdImageSerializer , CarCompanyCommentsSerializer
from .paginations import CarCompanyListPagination
from .permissions import IsManager
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




class ShowCarCompanyDetails(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CarCompanyWithImagesSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get(self, request, car_company_id):
        car_company = get_object_or_404(CarCompany, pk=car_company_id)
        images = CarCompanyImages.objects.filter(car_company=car_company_id)
        car_company.images = images
        serializer = self.serializer_class(car_company)
        return Response(serializer.data , status=status.HTTP_200_OK)


class ShowCars(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CarWithCarImagesSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get(self , request , car_company_id):
        cars = Car.objects.filter(car_company_id=car_company_id)
        for car in cars:
            images = CarImages.objects.filter(car=car.pk)
            car.images = images
        serializer = CarWithCarImagesSerializer(cars , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)

class ShowCarDetails(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CarWithCarImagesSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get(self, request, car_id):
        car = get_object_or_404(Car, pk=car_id)
        images = CarImages.objects.filter(car=car_id)
        car.images = images
        serializer = self.serializer_class(car)
        return Response(serializer.data , status=status.HTTP_200_OK)


class ShowCarReservationDetails(APIView):
    permission_classes = [IsAuthenticated , IsManager]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    serializer_class = CarReservationWithIdImageSerializer

    def get(self , request , car_id):
        reservation = get_object_or_404(CarReservation , car_id=car_id)
        images =  CarReservationIdImage.objects.filter(reservation_id=reservation.pk)
        reservation.images = images
        serializer = self.serializer_class(reservation)
        return Response(serializer.data , status=status.HTTP_200_OK)

class ShowCarCompanyReservationsDetails(APIView):
    permission_classes = [IsAuthenticated , IsManager]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    serializer_class = CarReservationWithIdImageSerializer

    def get(self , request , car_company_id):
        reservations = CarReservation.objects.filter(car_company_id=car_company_id)
        for reservation in reservations:
            images =  CarReservationIdImage.objects.filter(reservation_id=reservation.pk)
            reservation.images = images
        serializer = self.serializer_class(reservations , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)


class ShowCarCompanyComments(APIView):
    permission_classes = [IsAuthenticated , IsManager]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    serializer_class = CarCompanyCommentsSerializer

    def get(self , request , car_company_id):
        comments = CarCompanyComments.objects.filter(car_company_id=car_company_id)
        serializer = self.serializer_class(comments , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)