# Generated by Django 5.1.3 on 2024-11-16 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orphanage', '0003_child_delete_orphan_rename_donor_name_donation_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
    ]