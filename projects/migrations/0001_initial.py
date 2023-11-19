# Generated by Django 4.2.7 on 2023-11-11 16:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                (
                    "craft_type",
                    models.CharField(
                        choices=[
                            ("POT", "Pottery"),
                            ("KNI", "Knitting or Crochet"),
                            ("EMB", "Embroidery or Cross-stitch"),
                            ("SEW", "Sewing"),
                            ("WOO", "Woodworking"),
                            ("OTH", "Other"),
                        ],
                        max_length=3,
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("description", models.CharField(blank=True, max_length=250)),
                ("object_type", models.CharField()),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(null=True)),
                ("notes", models.TextField(blank=True)),
                ("clay_type", models.CharField(blank=True, max_length=30)),
                ("glaze_type", models.CharField(blank=True, max_length=30)),
                ("needle_size", models.CharField(blank=True, max_length=10)),
                ("yarn_weight", models.CharField(blank=True, max_length=30)),
                ("yarn_amount", models.CharField(blank=True, max_length=30)),
                ("yarn_color", models.CharField(blank=True, max_length=250)),
                ("fabric_info", models.CharField(blank=True, max_length=250)),
                ("floss_color", models.CharField(blank=True, max_length=250)),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("image_url", models.ImageField(upload_to="images")),
                ("cover_image", models.BooleanField()),
                (
                    "project_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="projects.project",
                    ),
                ),
            ],
        ),
    ]