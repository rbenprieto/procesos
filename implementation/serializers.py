from rest_framework import serializers
from .models import Ticket, Teams


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

    def create(self, validated_data):
        ticket = Ticket.objects.create(**validated_data)
        return ticket


class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = '__all__'
