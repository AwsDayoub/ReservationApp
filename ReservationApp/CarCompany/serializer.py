from rest_framework import serializers
from .models import CarCompany , CarCompanyImages , Car , CarImages , CarReservation , CarReservationIdImage , CarCompanyComments

class CarCompanySerializer(serializers.ModelSerializer):
    main_image = serializers.ImageField(max_length=None , use_url=True)

    class Meta:
        model = CarCompany
        fields = ['id', 'name' , 'email' , 'phone' , 'country' , 'city' , 'main_image' , 'date_created' , 'sum_of_rates' , 'number_of_rates']

class CarCompanyImagesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None , use_url=True)
    class Meta:
        model = CarCompanyImages
        fields = ['car_company' , 'image']


class CarCompanyWithImagesSerializer(serializers.ModelSerializer):
    main_image = serializers.ImageField(max_length=None , use_url=True)
    images = CarCompanyImagesSerializer(many=True , read_only=True)
    class Meta:
        model = CarCompany
        fields = ['id' , 'name' , 'email' , 'phone' , 'country' , 'city' , 'main_image' , 'date_created' , 'sum_of_rates' , 'number_of_rates' , 'images']


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id' , 'car_company_id' , 'name' , 'number' , 'car_type' , 'number_of_people_can_contain' , 'contain_baby_seat' , 'price' , 'description' , 'reserved']


class CarImagesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None , use_url=True)
    class Meta:
        model = CarImages
        fields = ['car' , 'image']


class CarWithCarImagesSerializer(serializers.ModelSerializer):
    images = CarImagesSerializer(many=True , read_only=True)
    class Meta:
        model = Car
        fields = ['id' , 'car_company_id' , 'name' , 'number' , 'car_type' , 'number_of_people_can_contain' , 'contain_baby_seat' , 'price' , 'description' , 'reserved' , 'images']


class CarReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarReservation
        fields = ['id' , 'car_company_id' , 'car_id' , 'user_id' , 'start_date' , 'end_date' , 'pickup_location' , 'delivery_location' , 'description']


class CarReservationIdImageserializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None , use_url=True)
    class Meta:
        model = CarReservationIdImage
        fields = '__all__'

class CarReservationWithIdImageSerializer(serializers.ModelSerializer):
    images = CarReservationIdImageserializer(many=True , read_only=True)
    class Meta:
        model = CarReservation
        fields = ['id' , 'car_company_id' , 'car_id' , 'user_id' , 'start_date' , 'end_date' , 'pickup_location' , 'delivery_location' , 'description' , 'images']


class CarCompanyCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarCompanyComments
        fields = '__all__'