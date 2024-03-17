from rest_framework import serializers
from .models import CarCompany

class CarCompanySerializer(serializers.ModelSerializer):
    main_image = serializers.ImageField(max_length=None , use_url=True)

    class Meta:
        model = CarCompany
        fields = '__all__'