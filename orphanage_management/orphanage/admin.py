from django.contrib import admin
from .models import Child
from .models import Donation


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'date_of_admission')
    search_fields = ('name',)
    list_filter = ('gender',)

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('donation_type', 'donor_name', 'amount', 'donation_date')