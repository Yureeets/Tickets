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

from mainapp.views import PassengerAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/passengers", PassengerAPIView.as_view(), name="passengers-list"),  # post and get passenger
    path("api/v1/passengers/<int:pk>", PassengerAPIView.as_view(), name="passenger-detail"),
    # get, put, delete data of specific passenger



    # path('flights/', FlightListCreateView.as_view(), name='flight-list-create'),
    # path('flights/<int:pk>/', FlightDetailView.as_view(), name='flight-detail'),
    #
    # path('tickets/', TicketListCreateView.as_view(), name='ticket-list-create'),
    # path('tickets/<int:pk>/', TicketDetailView.as_view(), name='ticket-detail'),
]
