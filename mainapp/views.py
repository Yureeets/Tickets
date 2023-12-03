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

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Passenger
from .serializers import PassengerSerializer

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
