# Generated by Django 5.1.3 on 2024-11-16 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orphanage', '0002_donation_orphan_available_for_adoption_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_admission', models.DateField()),
                ('guardian_contact', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Orphan',
        ),
        migrations.RenameField(
            model_name='donation',
            old_name='donor_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='date_of_donation',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='details',
        ),
        migrations.AddField(
            model_name='donation',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='donation',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='donation',
            name='email',
            field=models.EmailField(default='unknown@example.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='donation',
            name='donation_type',
            field=models.CharField(choices=[('Money', 'Money'), ('Clothes', 'Clothes'), ('Food', 'Food'), ('Other', 'Other')], max_length=20),
        ),
    ]
