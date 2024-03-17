from django.urls import path
from . import views

urlpatterns = [
    path('search_for_car_companies/<str:word>', views.SearchForCarCompanies.as_view())
]