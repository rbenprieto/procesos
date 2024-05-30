from rest_framework import viewsets, status
from django.db.models import Max
from rest_framework.response import Response
from .models import Ticket, Teams
from .serializers import TicketSerializer, TeamsSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def perform_create(self, serializer):
        max_ticket_number = Ticket.objects.aggregate(Max('ticket_number'))['ticket_number__max']
        new_ticket_number = (max_ticket_number or 0) + 1
        serializer.save(ticket_number=new_ticket_number)


class TeamsViewSet(viewsets.ModelViewSet):
    queryset = Teams.objects.all()
    serializer_class = TeamsSerializer