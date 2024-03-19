from django.urls import path
from . import views

urlpatterns = [
    path('search_for_car_companies/<str:word>/', views.SearchForCarCompanies.as_view()),
    path('show_car_comapnies/', views.ShowCarCompanies.as_view()),
    path('show_car_company_details/<int:car_company_id>/', views.ShowCarCompanyDetails.as_view()),
    path('show_cars/<int:car_company_id>/', views.ShowCars.as_view()),
    path('show_car_details/<int:car_id>/', views.ShowCarDetails.as_view()),
    path('show_car_reservation_details/<int:car_id>/', views.ShowCarReservationDetails.as_view()),
    path('show_car_company_reservations_details/<int:car_company_id>/', views.ShowCarCompanyReservationsDetails.as_view()),
    path('show_car_company_comments/<int:car_company_id>/', views.ShowCarCompanyComments.as_view())
]