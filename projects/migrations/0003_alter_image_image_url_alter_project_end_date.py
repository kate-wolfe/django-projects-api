# Generated by Django 4.2.7 on 2023-11-19 18:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0002_alter_project_clay_type_alter_project_glaze_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="image_url",
            field=models.ImageField(upload_to="static"),
        ),
        migrations.AlterField(
            model_name="project",
            name="end_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]