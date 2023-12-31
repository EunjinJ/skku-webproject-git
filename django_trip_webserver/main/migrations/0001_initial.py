# Generated by Django 4.2.5 on 2023-10-18 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AreaL",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("area_l_name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="TripCategory",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("trip_category_name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="AreaM",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("area_m_name", models.CharField(max_length=255)),
                (
                    "area_l_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="aream_set",
                        to="main.areal",
                    ),
                ),
            ],
        ),
    ]
