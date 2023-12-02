from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Ticket, Passenger, Flight
from .serializer import TicketSerializer


class TicketAPIView(APIView):
    def get(self, request):
        lst = Ticket.objects.all().values()
        return Response({"posts": lst})

    def post(self, request):
        post_new = Ticket.objects.create(
            flight=request.data['flight'],
            passengers=request.data['passengers'],
            seet_class=request.data['seet_class'],
            booking_date=request.data['booking_date'],
            status=request.data['status'],
        )
        return Response({"ticket": model_to_dict(post_new)})


class PassengerAPIView(APIView):
    def get(self, request):
        lst = Passenger.objects.all().values()
        return Response({"posts": lst})

    def post(self, request):
        post_new = Passenger.objects.create(
            first_name=request.data['first_name'],
            last_name=request.data['last_name'],
            gender=request.data['gender'],
        )
        return Response({"Passengers": model_to_dict(post_new)})

# class TicketAPIView(generics.ListAPIView):
#     queryset = Ticket.objects.all()
#     serializer_class = TicketSerializer
