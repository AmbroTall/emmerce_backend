# Generated by Django 5.1.4 on 2025-01-06 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crm", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="lead",
            name="company",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
