# Generated by Django 4.2.5 on 2023-10-18 01:54

import board.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("review_title", models.CharField(max_length=255)),
                ("review_content", models.TextField()),
                ("review_time", models.DateTimeField(auto_now_add=True)),
                (
                    "review_image1",
                    models.ImageField(blank=True, null=True, upload_to="review_image"),
                ),
                (
                    "review_image2",
                    models.ImageField(blank=True, null=True, upload_to="review_image"),
                ),
                (
                    "review_image3",
                    models.ImageField(blank=True, null=True, upload_to="review_image"),
                ),
                (
                    "review_image4",
                    models.ImageField(blank=True, null=True, upload_to="review_image"),
                ),
                (
                    "review_image5",
                    models.ImageField(blank=True, null=True, upload_to="review_image"),
                ),
                ("is_deleted", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="Trip",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("trip_category_detail", models.CharField(max_length=255)),
                ("trip_name", models.CharField(max_length=255)),
                ("trip_address", models.TextField()),
                ("trip_time", models.CharField(max_length=512, null=True)),
                ("trip_phone", models.CharField(max_length=255)),
                ("trip_homepage", models.TextField()),
                ("is_deleted", models.BooleanField(default=False)),
                (
                    "area_m",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="main.aream",
                    ),
                ),
                (
                    "trip_category_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="main.tripcategory",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TripComment",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("trip_comment_content", models.TextField()),
                ("trip_commnet_time", models.DateTimeField(auto_now_add=True)),
                (
                    "trip_comment_star",
                    models.IntegerField(validators=[board.models.validate_star_range]),
                ),
                ("is_deleted", models.BooleanField()),
                (
                    "trip_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="tripcomment_set",
                        to="board.trip",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ReviewRecommend",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("review_recommend", models.BooleanField()),
                ("is_deleted", models.BooleanField()),
                (
                    "review_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="board.review",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ReviewComment",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("review_comment_content", models.TextField()),
                ("review_comment_time", models.DateTimeField(auto_now_add=True)),
                ("is_deleted", models.BooleanField()),
                (
                    "review_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="board.review",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="review",
            name="trip_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="review_set",
                to="board.trip",
            ),
        ),
        migrations.AddField(
            model_name="review",
            name="user_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.CreateModel(
            name="Menu",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("menu_content", models.CharField(max_length=255)),
                ("menu_price", models.IntegerField()),
                (
                    "trip_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="board.trip",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Info",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("info_content", models.TextField()),
                (
                    "trip_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="board.trip",
                    ),
                ),
            ],
        ),
    ]
