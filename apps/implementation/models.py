from django.db import models


class Teams(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Ticket(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    ticket_number = models.IntegerField()
    date_generation = models.DateField()
    client_name = models.CharField(max_length=255)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    category_problem = models.CharField(max_length=25)
    description = models.TextField()
    team = models.ForeignKey(Teams, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    solucionado_cs = models.BooleanField(default=False)
    cs_management_date = models.DateTimeField(null=True, blank=True)
    solucionado_cs_and_ma = models.BooleanField(default=False)
    cs_and_ma_management_date = models.DateTimeField(null=True, blank=True)
    assigned_date = models.DateTimeField(null=True, blank=True)
    review_status_date = models.DateTimeField(null=True, blank=True)
    solution_date = models.DateTimeField(null=True, blank=True)
    closed_date = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.ticket_number)
