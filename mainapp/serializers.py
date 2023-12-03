from datetime import datetime
from django.utils import timezone

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import Ticket, Passenger, Flight


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = "__all__"


class TicketSerializer(serializers.ModelSerializer):
    passengers = PassengerSerializer(many=True)

    class Meta:
        model = Ticket
        fields = '__all__'

    def create(self, validated_data):
        passengers_data = validated_data.pop('passengers')
        ticket = Ticket.objects.create(**validated_data, booking_date=timezone.now())

        for passenger_data in passengers_data:
            passenger = Passenger.objects.create(**passenger_data)
            ticket.passengers.add(passenger)

        return ticket

    def update(self, instance, validated_data):
        passengers_data = validated_data.pop('passengers')
        instance = super().update(instance, validated_data)

        # Handle the update logic for passengers if needed
        # For example, you might want to delete existing passengers and add new ones

        instance.passengers.clear()

        for passenger_data in passengers_data:
            passenger = Passenger.objects.create(**passenger_data)
            instance.passengers.add(passenger)

        return instance


# def encode():
#     model = PassengerModel("Yura", "Polulikh", "male")
#     model_cl = PassengerSerializer(model)
#     print(model_cl.data, type(model_cl.data), sep=' ')
#     json = JSONRenderer().render(model_cl.data)
#     print(json)
# class TicketSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ticket
#         fields = "__all__"
#
#
# class PassengerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Passenger
#         fields = "__all__"
