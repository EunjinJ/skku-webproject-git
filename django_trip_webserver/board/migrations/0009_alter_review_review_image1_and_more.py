# Generated by Django 4.2.5 on 2023-10-17 06:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("board", "0008_alter_review_review_image1_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="review_image1",
            field=models.ImageField(blank=True, null=True, upload_to="review_image"),
        ),
        migrations.AlterField(
            model_name="review",
            name="review_image2",
            field=models.ImageField(blank=True, null=True, upload_to="review_image"),
        ),
        migrations.AlterField(
            model_name="review",
            name="review_image3",
            field=models.ImageField(blank=True, null=True, upload_to="review_image"),
        ),
        migrations.AlterField(
            model_name="review",
            name="review_image4",
            field=models.ImageField(blank=True, null=True, upload_to="review_image"),
        ),
        migrations.AlterField(
            model_name="review",
            name="review_image5",
            field=models.ImageField(blank=True, null=True, upload_to="review_image"),
        ),
    ]
