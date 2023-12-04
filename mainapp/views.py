from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Ticket, Passenger, Flight
from .serializers import PassengerSerializer

from rest_framework import generics
from .models import Passenger, Flight, Ticket
from .serializers import PassengerSerializer, FlightSerializer, TicketSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Passenger
from .serializers import PassengerSerializer
from rest_framework import serializers




def index(request):
    return render(request,"index.html")


class PassengerAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            passenger = get_object_or_404(Passenger, pk=pk)
            serializer = PassengerSerializer(passenger)
            return Response(serializer.data)
        else:
            passengers = Passenger.objects.all()
            serializer = PassengerSerializer(passengers, many=True)
            return Response({"passengers": serializer.data})

    def post(self, request, *args, **kwargs):
        serializer = PassengerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_passenger = serializer.save()
        return Response({"passenger": PassengerSerializer(new_passenger).data}, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        passenger = get_object_or_404(Passenger, pk=pk)
        serializer = PassengerSerializer(passenger, data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_passenger = serializer.save()
        return Response({"passenger": PassengerSerializer(updated_passenger).data})

    def delete(self, request, pk):
        passenger = get_object_or_404(Passenger, pk=pk)
        passenger.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FlightAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            flight = get_object_or_404(Flight, pk=pk)
            serializer = FlightSerializer(flight)
            return Response(serializer.data)
        else:
            flights = Flight.objects.all()
            serializer = FlightSerializer(flights, many=True)
            return Response({"flights": serializer.data})

    def post(self, request, *args, **kwargs):
        serializer = FlightSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_flight = serializer.save()
        return Response({"flight": FlightSerializer(new_flight).data}, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        flight = get_object_or_404(Flight, pk=pk)
        serializer = FlightSerializer(flight, data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_flight = serializer.save()
        return Response({"flight": FlightSerializer(updated_flight).data})

    def delete(self, request, pk):
        flight = get_object_or_404(Flight, pk=pk)
        flight.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FlightSearchByCitiesAPIView(APIView):
    def get(self, request, origin_city, destination_city):
        flights = Flight.objects.filter(origin_city=origin_city, destination_city=destination_city)
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data)


class TicketListAPIView(APIView):
    def get(self, request):
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TicketSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        new_ticket = serializer.save()
        new_ticket_serializer = TicketSerializer(new_ticket)

        return Response(new_ticket_serializer.data, status=status.HTTP_201_CREATED)


class TicketDetailAPIView(APIView):
    def get(self, request, pk):
        ticket = get_object_or_404(Ticket, pk=pk)
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)

    def put(self, request, pk):
        ticket = get_object_or_404(Ticket, pk=pk)
        serializer = TicketSerializer(ticket, data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_ticket = serializer.save()
        return Response(TicketSerializer(updated_ticket).data)

    def delete(self, request, pk):
        ticket = get_object_or_404(Ticket, pk=pk)
        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





# class TicketAPIView(APIView):

# class TicketAPIView(APIView):
#     def get(self, request):
#         lst = Ticket.objects.all().values()
#         return Response({"posts": lst})
#
#     def post(self, request):
#         post_new = Ticket.objects.create(
#             flight=request.data['flight'],
#             passengers=request.data['passengers'],
#             seet_class=request.data['seet_class'],
#             booking_date=request.data['booking_date'],
#             status=request.data['status'],
#         )
#         return Response({"ticket": model_to_dict(post_new)})


# class PassengerAPIView(APIView):
#     def get(self, request):
#         w = Passenger.objects.all()
#         return Response({"posts": PassengerSerializer(w, many=True).data})
#
#     def post(self, request):
#
#         serializer = PassengerSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         post_new = Passenger.objects.create(
#             first_name=request.data['first_name'],
#             last_name=request.data['last_name'],
#             gender=request.data['gender'],
#         )
#         return Response({"Passengers": PassengerSerializer(post_new).data})

# class TicketAPIView(generics.ListAPIView):
#     queryset = Ticket.objects.all()
#     serializer_class = TicketSerializer
