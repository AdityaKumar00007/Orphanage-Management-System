from django.shortcuts import render, redirect
from .models import Child, Donation
from django.http import HttpResponse
from .forms import DonationForm
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404

def home(request):
    return render(request, 'home.html')

def adoption_page(request):
    children = Child.objects.all()
    return render(request, 'adoption_page.html', {'children': children})

def donate(request): 
    if request.method == 'POST':
        form = DonationForm(request.POST)  # Use the form object directly
        if form.is_valid():
            # Save the form data
            donation = form.save()
            # Pass the donation details to the success page
            return render(request, 'donation_success.html', {
                'name': donation.donor_name,
                'amount': donation.amount
            })
        else:
            # Return errors if form validation fails
            return render(request, 'donate.html', {'form': form})
    else:
        # For GET requests, render an empty form
        form = DonationForm()
        return render(request, 'donate.html', {'form': form})

def adoption(request):
    children = Child.objects.all()
    return render(request, 'adoption.html', {'children': children})    

def adopt_child(request, child_id):
    child = get_object_or_404(Child, id=child_id)

    if child.is_adopted:
        return render(request, 'adoption_error.html', {'child': child})

    # Generate appointment details
    appointment_date = datetime.now() + timedelta(days=7)  # Set 7 days from now
    formatted_date = appointment_date.strftime("%d-%m-%Y")
    formatted_time = appointment_date.strftime("%H:%M %p")

    # Optionally update the child's status (if admin-confirmed later)
    child.is_adopted = True
    child.save()

    return render(request, 'adoption_confirmation.html', {
        'child': child,
        'appointment_date': formatted_date,
        'appointment_time': formatted_time,
    })