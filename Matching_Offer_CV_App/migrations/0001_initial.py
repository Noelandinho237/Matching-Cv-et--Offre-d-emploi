# Generated by Django 4.2.15 on 2024-08-19 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cv",
            fields=[
                ("id_cv", models.AutoField(primary_key=True, serialize=False)),
                ("description_cv", models.FileField(upload_to="Files/CVs")),
            ],
        ),
        migrations.CreateModel(
            name="Offer",
            fields=[
                ("id_offer", models.AutoField(primary_key=True, serialize=False)),
                ("title_offer", models.CharField(max_length=255)),
                ("description_offer", models.FileField(upload_to="Files/Offers")),
            ],
        ),
    ]
