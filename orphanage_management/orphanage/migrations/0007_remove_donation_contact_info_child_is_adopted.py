# Generated by Django 5.1.3 on 2024-11-18 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orphanage', '0006_rename_created_at_donation_donation_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='contact_info',
        ),
        migrations.AddField(
            model_name='child',
            name='is_adopted',
            field=models.BooleanField(default=False),
        ),
    ]
