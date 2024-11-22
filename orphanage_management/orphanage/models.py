from django.db import models


class Child(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_admission = models.DateField()
    guardian_contact = models.CharField(max_length=15, null=True, blank=True)
    is_adopted = models.BooleanField(default=False)  # Track adoption status

    def __str__(self):
        return self.name


class Donation(models.Model):
    DONATION_TYPES = [
        ('money', 'Money'),
        ('clothes', 'Clothes'),
        ('toys', 'Toys'),
        ('school_supplies', 'School Supplies'),
        ('food', 'Food Items'),
        ('blankets', 'Blankets'),
    ]
    donor_name = models.CharField(max_length=100)
    donation_type = models.CharField(max_length=50, choices=DONATION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    donation_date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()

    def __str__(self):
        return f"{self.donation_type} by {self.donor_name}"