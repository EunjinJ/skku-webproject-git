# Generated by Django 4.2.5 on 2023-10-14 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
        ("board", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="trip",
            name="trip_break_end",
        ),
        migrations.RemoveField(
            model_name="trip",
            name="trip_break_start",
        ),
        migrations.RemoveField(
            model_name="trip",
            name="trip_closed",
        ),
        migrations.RemoveField(
            model_name="trip",
            name="trip_last_order",
        ),
        migrations.RemoveField(
            model_name="trip",
            name="trip_open",
        ),
        migrations.AddField(
            model_name="trip",
            name="area_m_ID",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="main.aream"
            ),
        ),
        migrations.AddField(
            model_name="trip",
            name="trip_time",
            field=models.CharField(max_length=512, null=True),
        ),
    ]
# Generated by Django 4.2.5 on 2023-10-14 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
        ("board", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="trip",
            name="trip_break_end",
        ),
        migrations.RemoveField(
            model_name="trip",
            name="trip_break_start",
        ),
        migrations.RemoveField(
            model_name="trip",
            name="trip_closed",
        ),
        migrations.RemoveField(
            model_name="trip",
            name="trip_last_order",
        ),
        migrations.RemoveField(
            model_name="trip",
            name="trip_open",
        ),
        migrations.AddField(
            model_name="trip",
            name="area_m_ID",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="main.aream"
            ),
        ),
        migrations.AddField(
            model_name="trip",
            name="trip_time",
            field=models.CharField(max_length=512, null=True),
        ),
    ]
