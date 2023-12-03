from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import Ticket, Passenger, Flight


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = "__all__"


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = "__all__"


class TicketSerializer(serializers.ModelSerializer):
    flight = FlightSerializer()
    passengers = PassengerSerializer(many=True)

    class Meta:
        model = Ticket
        fields = "__all__"

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
