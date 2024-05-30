from django.db import models


class Teams(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    name = models.CharField(max_length=255)


class Ticket(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    ticket_number = models.IntegerField()
    date_generation = models.DateField()
    client_name = models.CharField(max_length=255)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    category_problem = models.CharField(max_length=25)
    description = models.TextField()
    team = models.ForeignKey(Teams, on_delete=models.SET_NULL, null=True, blank=True)
