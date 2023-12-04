"""
URL configuration for Tickets project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainapp.views import PassengerAPIView, FlightAPIView, FlightSearchByCitiesAPIView, TicketListAPIView, \
    TicketDetailAPIView, index
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Flight Booking API",
        default_version='v1',
        description="API for managing flights, passengers, and tickets",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("",index),

    path("api/v1/passengers", PassengerAPIView.as_view(), name="passengers-list"),  # post and get passenger
    path("api/v1/passengers/<int:pk>", PassengerAPIView.as_view(), name="passenger-detail"),
    # get, put, delete data of specific passenger

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # swagger url
    path('api/v1/flights/', FlightAPIView.as_view(), name='flight-list-create'),
    path('api/v1/flights/<int:pk>', FlightAPIView.as_view(), name='flight-detail'),
    path('api/v1/flights/cities/<str:origin_city>/<str:destination_city>/', FlightSearchByCitiesAPIView.as_view(),
         name='flight-search-by-cities'),

    path('api/v1/tickets/', TicketListAPIView.as_view(), name='ticket-list'),
    path('api/v1/tickets/<int:pk>', TicketDetailAPIView.as_view(), name='ticket-detail'),
]

