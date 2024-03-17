from django.urls import path
from . import views

urlpatterns = [
    path('search_for_events/<str:word>', views.SearchForEvents.as_view())
]