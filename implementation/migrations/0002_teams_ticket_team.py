# Generated by Django 5.0.3 on 2024-05-28 03:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("implementation", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Teams",
            fields=[
                (
                    "id",
                    models.AutoField(
                        editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name="ticket",
            name="team",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="implementation.teams",
            ),
        ),
    ]
